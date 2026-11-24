<#
.SYNOPSIS
  Link sis + core (CONTENTY) skills and plugins on Windows 11 for Antigravity, Claude Code, and OpenCode.
.DESCRIPTION
  Idempotent setup script. Uses Junctions/copies so Windows Developer Mode is NOT required.
  Does NOT download AI models or install Python packages automatically.
#>
param(
  [ValidateSet("antigravity", "claude", "opencode", "all")]
  [string]$Target = "all"
)

$ErrorActionPreference = "Stop"
$Root = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path
$Core = Join-Path $Root "core"

if (-not (Test-Path (Join-Path $Core "skills"))) {
  Write-Error "core/ alt modulu bos gorunuyor. Once calistir: git submodule update --init --recursive"
  exit 1
}

function Ensure-JunctionOrCopy {
  param([string]$Source, [string]$Dest)
  if (Test-Path $Dest) {
    $item = Get-Item $Dest -Force
    if ($item.Attributes -band [IO.FileAttributes]::ReparsePoint) {
      cmd /c rmdir "$Dest" | Out-Null
    } else {
      Remove-Item -Path $Dest -Recurse -Force
    }
  }
  try {
    New-Item -ItemType Junction -Path $Dest -Target $Source | Out-Null
  } catch {
    Copy-Item -Path $Source -Destination $Dest -Recurse -Force
  }
}

function Link-Antigravity {
  $dest = Join-Path $HOME ".gemini\config\plugins\contenty-studio"
  New-Item -ItemType Directory -Path $dest -Force | Out-Null
  Copy-Item (Join-Path $Core "plugins\contenty-studio\plugin.json") $dest -Force
  Copy-Item (Join-Path $Core "plugins\contenty-studio\README.md") $dest -Force
  Ensure-JunctionOrCopy -Source (Join-Path $Core "plugins\contenty-studio\rules") -Dest (Join-Path $dest "rules")
  Ensure-JunctionOrCopy -Source (Join-Path $Core "skills") -Dest (Join-Path $dest "skills")
  Write-Host "[Antigravity] Eklenti ve core skill'ler baglandi -> $dest"
}

function Link-Claude {
  $dest = Join-Path $HOME ".claude\skills"
  New-Item -ItemType Directory -Path $dest -Force | Out-Null
  Get-ChildItem (Join-Path $Core "skills") -Directory | ForEach-Object {
    Ensure-JunctionOrCopy -Source $_.FullName -Dest (Join-Path $dest $_.Name)
  }
  Write-Host "[Claude Code] Core skill'ler baglandi -> $dest"
}

function Link-OpenCode {
  Write-Host "[OpenCode] Kok AGENTS.md -> CLAUDE.md dogrudan okunur (ek baglanti gerekmez)."
}

switch ($Target) {
  "antigravity" { Link-Antigravity }
  "claude"      { Link-Claude }
  "opencode"    { Link-OpenCode }
  "all" {
    Link-Antigravity
    Link-Claude
    Link-OpenCode
  }
}

Write-Host "Not: Hicbir AI modeli veya pip paketi otomatik indirilmedi (playbooks/tts-and-music-stack.md)."
