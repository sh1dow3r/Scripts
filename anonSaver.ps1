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
