<#
.SYNOPSIS
Verifies a PL Sweep installer against its downloaded SHA-256 sidecar.
.DESCRIPTION
Reads both files locally. It does not download, install, or execute anything.
#>
[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)]
    [string] $Installer,
    [string] $Checksum
)

$ErrorActionPreference = 'Stop'
$installerPath = (Resolve-Path -LiteralPath $Installer -ErrorAction Stop).ProviderPath
$installerName = [IO.Path]::GetFileName($installerPath)
if ($installerName -notmatch '^PLSweep-Setup-\d+\.\d+\.\d+\.exe$') {
    throw 'Expected a PLSweep-Setup-X.Y.Z.exe installer filename.'
}
if ([string]::IsNullOrWhiteSpace($Checksum)) {
    $Checksum = "$installerPath.sha256"
}
$checksumPath = (Resolve-Path -LiteralPath $Checksum -ErrorAction Stop).ProviderPath
$checksumText = (Get-Content -LiteralPath $checksumPath -Raw).Trim()
$escapedName = [regex]::Escape($installerName)
if ($checksumText -notmatch "\A([0-9a-fA-F]{64})[ \t]+\*?$escapedName\z") {
    throw 'Checksum must contain one SHA-256 value and the exact installer filename.'
}
$expectedHash = $Matches[1]
$actualHash = (Get-FileHash -LiteralPath $installerPath -Algorithm SHA256).Hash
if (-not [string]::Equals($actualHash, $expectedHash, [StringComparison]::OrdinalIgnoreCase)) {
    throw 'SHA-256 mismatch. Do not run this installer; download both assets again from the official release.'
}
Write-Output "SHA-256 verified: $installerName"
Write-Output 'This verifies a matching checksum, not Authenticode signing or publisher identity.'
