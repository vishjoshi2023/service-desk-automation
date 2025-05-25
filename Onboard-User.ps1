<#
.SYNOPSIS
Creates an AD user, assigns an O365 licence and opens a ServiceNow ticket.
.DESCRIPTION
Demo script for portfolio — **NOT** production ready.
#>

param(
    [Parameter(Mandatory)]
    [string]$UserName,
    [string]$DisplayName,
    [string]$Email
)

Write-Host "📂 Creating AD account for $DisplayName"
# New-ADUser -Name $DisplayName -SamAccountName $UserName …

Write-Host "🔑 Assigning M365 licence"
# Set-MsolUserLicense …

Write-Host "📝 Raising ServiceNow ticket"
# Invoke-RestMethod -Uri $snUrl -Body $json …

Write-Host "✅ On-boarding complete"
