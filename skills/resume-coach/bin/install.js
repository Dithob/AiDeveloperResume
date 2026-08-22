#!/usr/bin/env node
'use strict';

const fs = require('fs');
const path = require('path');
const os = require('os');

const SKILL_NAME = 'resume-coach';
const COPY_ITEMS = ['SKILL.md', 'references', 'assets', 'agents'];

const USAGE = `resume-coach-skill — install the resume-coach skill into an agent tool's skills directory.

Usage:
  npx resume-coach-skill [options]

Options:
  --target <name>     Target tool preset. One of:
                        codebuddy          ~/.codebuddy/skills/resume-coach   (default, user-level)
                        codebuddy:project  <cwd>/.codebuddy/skills/resume-coach
                        claude             ~/.claude/skills/resume-coach
                        agents             ~/.agents/skills/resume-coach
  --dir <path>        Install into an explicit directory.
  --symlink           Symlink files instead of copying (dev mode).
  --force             Overwrite an existing installation.
  --help              Show this help.
`;

function argValue(args, flag) {
  const i = args.indexOf(flag);
  return i !== -1 && args[i + 1] ? args[i + 1] : null;
}

function resolveTargetDir(args) {
  const explicit = argValue(args, '--dir');
  if (explicit) return path.resolve(explicit);

  const target = argValue(args, '--target') || 'codebuddy';
  const home = os.homedir();
  switch (target) {
    case 'codebuddy':
      return path.join(home, '.codebuddy', 'skills', SKILL_NAME);
    case 'codebuddy:project':
    case 'project':
    case 'local':
      return path.join(process.cwd(), '.codebuddy', 'skills', SKILL_NAME);
    case 'claude':
      return path.join(home, '.claude', 'skills', SKILL_NAME);
    case 'agents':
      return path.join(home, '.agents', 'skills', SKILL_NAME);
    default:
      // assume an explicit path was passed via --target
      return path.resolve(target);
  }
}

function copyDir(src, dest) {
  fs.mkdirSync(dest, { recursive: true });
  for (const entry of fs.readdirSync(src, { withFileTypes: true })) {
    const s = path.join(src, entry.name);
    const d = path.join(dest, entry.name);
    if (entry.isDirectory()) copyDir(s, d);
    else fs.copyFileSync(s, d);
  }
}

function linkOrCopy(src, dest, useSymlink) {
  const isDir = fs.statSync(src).isDirectory();
  if (useSymlink) {
    if (fs.existsSync(dest)) fs.rmSync(dest, { recursive: true, force: true });
    // On Windows, directory symlinks need 'junction' (no admin rights required).
    const type =
      process.platform === 'win32' && isDir ? 'junction' : isDir ? 'dir' : 'file';
    fs.symlinkSync(src, dest, type);
  } else if (isDir) {
    copyDir(src, dest);
  } else {
    fs.copyFileSync(src, dest);
  }
}

function main() {
  const args = process.argv.slice(2);
  if (args.includes('--help') || args.includes('-h')) {
    console.log(USAGE);
    process.exit(0);
  }

  const useSymlink = args.includes('--symlink');
  const force = args.includes('--force');
  const skillRoot = path.resolve(__dirname, '..');
  const targetDir = resolveTargetDir(args);

  if (!fs.existsSync(path.join(skillRoot, 'SKILL.md'))) {
    console.error('✗ SKILL.md not found in package root: ' + skillRoot);
    process.exit(1);
  }

  if (fs.existsSync(targetDir) && !force) {
    console.error('✗ Target already exists: ' + targetDir);
    console.error('  Re-run with --force to overwrite, or --dir <path> to pick another location.');
    process.exit(1);
  }

  fs.mkdirSync(targetDir, { recursive: true });
  for (const item of COPY_ITEMS) {
    const src = path.join(skillRoot, item);
    if (!fs.existsSync(src)) continue;
    linkOrCopy(src, path.join(targetDir, item), useSymlink);
  }

  console.log('✓ resume-coach installed to: ' + targetDir);
  console.log('  Restart/refresh the agent session so it can discover the skill.');
}

main();
