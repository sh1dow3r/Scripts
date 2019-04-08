$appCmd = "C:\windows\system32\inetsrv\appcmd.exe"
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



    
