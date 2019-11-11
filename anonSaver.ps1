
<#
.Synopsis
   This mini HIDS tool checks for anonymous ftp and disables it
.DESCRIPTION
   This mini HIDS tool logs as anonmoys user and check if it successfully 
   logged in or not. If the user logged in, it notifies you as devloper.
   The tools also allows you to disble ftp anonymous on ISS.
.EXAMPLE
   anonyFTP.ps1 <ftp_ip_address> -v
.EXAMPLE
   anonyFTP.ps1 <ftp_ip_address> -f -y 
.INPUTS
  usage: hi.py [-h] [--verbose] [--version] [-f] [-y] [-n] ftp_ip

positional arguments:
  ftp_ip         display a square of a given number

optional arguments:
  -h, --help     show this help message and exit
  --verbose, -v  increase output verbosity
  --version      Show version.
  -f, --fix      fix the ftp anonymous login
  -y, --yes      does not prompt the user for confirming the fix
  -n             show but not run the command to fix the ftp anonymous login
#>

<#$appCmd = "C:\windows\system32\inetsrv\appcmd.exe"
& $appCmd --% set config /section:anonymousAuthentication /enabled:false

function help{
       Write-Host("help")
}
function main
{
param(
       [Parameter(Mandatory=$true, Position=0, )] $ftpServer,
       $help,
       $verbose,
       $fix,
       $y,
       $n
)
}
#>
function Verb-Noun
{
    [CmdletBinding(DefaultParameterSetName='Parameter Set 1', 
                  SupportsShouldProcess=$true, 
                  PositionalBinding=$false,
                  HelpUri = 'http://www.microsoft.com/',
                  ConfirmImpact='Medium')]
    [Alias()]
    [OutputType([String])]
    Param
    (
        # Param1 help description
        [Parameter(Mandatory=$true, 
                   ValueFromPipeline=$true,
                   ValueFromPipelineByPropertyName=$true, 
                   ValueFromRemainingArguments=$false, 
                   Position=0,
                   ParameterSetName='Parameter Set 1')]
        [ValidateNotNull()]
        [ValidateNotNullOrEmpty()]
        [ValidateCount(0,5)]
        [ValidateSet("sun", "moon", "earth")]
        [Alias("p1")] 
        $Param1,

        # Param2 help description
        [Parameter(ParameterSetName='Parameter Set 1')]
        [AllowNull()]
        [AllowEmptyCollection()]
        [AllowEmptyString()]
        [ValidateScript({$true})]
        [ValidateRange(0,5)]
        [int]
        $Param2,

        # Param3 help description
        [Parameter(ParameterSetName='Another Parameter Set')]
        [ValidatePattern("[a-z]*")]
        [ValidateLength(0,15)]
        [String]
        $Param3
    )

    Begin
    {
    }
    Process
    {
        if ($pscmdlet.ShouldProcess("Target", "Operation"))
        {
        }
    }
    End
    {
    }
}
$appCmd = "C:\windows\system32\inetsrv\appcmd.exe"
& $appCmd --% set config /section:anonymousAuthentication /enabled:false

function help{
       Write-Host("help")
}
function main
{
param(
       [Parameter(Mandatory=$true, Position=0,Helpmessage="Please enter you ftp setver IP address?" )] $ftpServer,
       $help,
       $verbose,
       $fix,
       $y,
       $n
)
}
function New-FtpRequest ($sourceUri, $method, $username, $password) {
    $ftprequest = [System.Net.FtpWebRequest]::Create($sourceuri)
    $ftprequest.Method = $method
    $ftprequest.Credentials = New-Object System.Net.NetworkCredential($username,$password)
    return $ftprequest
}

function Send-FtpRequest($ftpRequest) {
    Write-Host "$($ftpRequest.Method) for '$($ftpRequest.RequestUri)' executing"
    $response = $ftprequest.GetResponse()
    $closed = $response.Close()
    Write-Host "Response: '$($response.StatusDescription)'"
    return $response
}

function Parse-Output($output, [System.Management.Automation.SwitchParameter]$file, [System.Management.Automation.SwitchParameter]$directory) {
    $entities = @()
    foreach ($CurLine in $output) {
        $LineTok = ($CurLine -split '\ +')
        $currentEntity = $LineTok[8..($LineTok.Length-1)]
        if(-not $currentEntity) { continue }
        $isDirectory = $LineTok[0].StartsWith("d")
        if($file -and -not $isDirectory) {
            $entities += $currentEntity
        } elseif($directory -and $isDirectory) {
            $entities += $currentEntity
        }
    }
    return $entities
}
