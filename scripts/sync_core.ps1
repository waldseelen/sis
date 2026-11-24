<#
.SYNOPSIS
  Pull latest CONTENTY core changes into sis/core submodule on Windows.
#>
$ErrorActionPreference = "Stop"
$Root = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path
Push-Location $Root
try {
  git submodule sync -- core
  git submodule update --init --remote --merge core
  Write-Host "core/ alt modulu guncellendi:"
  git submodule status core
} finally {
  Pop-Location
}
