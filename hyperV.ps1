
#Uncomment the following line to install CentOS7 image in the right folder real quitck
#wget "http://mirror.es.its.nyu.edu/centos/7.6.1810/isos/x86_64/CentOS-7-x86_64-Minimal-1810.iso" -OutFile "C:\Users\Administrator\Desktop\CentOS7.iso"

#The path used for the vms
$VMPath = "C:\Users\Administrator\Desktop\Demo\VM"

#ISO path for the VMS
$ISOPath = "C:\Users\Administrator\Desktop\CentOS7.iso"

#startp memory to install the VM
$StartupMemory = 1GB
$VMSwitchName  =  (Get-VMSwitch).Name
$VMStoragePath = "C:\Users\Administrator\Desktop\VM\$VMName"
$MinimumMemory = 1GB
$MaximumMemory = 2GB
$VHDStoragePath =  "C:\Users\Administrator\Desktop\VM\$VMName.vhdx"
$ISOPath = "C:\Users\Administrator\Desktop\CentOS7.iso"

#Options for basic or advance VM
$OPT = READ-HOST "Do you want a [basic] or [advance] VM?"
   
if ($OPT -eq "basic") {
    #getting the VMName
    [string]$VMName = READ-HOST "What is the VM name?"
    #setting up the VM with default stuff 
    $VM = New-VM -Name $VMName -MemoryStartupBytes $StartupMemory -SwitchName $VMSwitchName -Path $VMStoragePath -Generation 2 -NoVHD
	Set-VMMemory -VM $VM -DynamicMemoryEnabled $true -MinimumBytes $MinimumMemory -MaximumBytes $MaximumMemory
	Set-VMProcessor -VM $VM -Count 2
	Start-VM -VM $VM
	Stop-VM -VM $VM -Force
	New-VHD -Path $VHDStoragePath -SizeBytes $VHDXSizeBytes -Dynamic -BlockSizeBytes 1MB
	$VMVHD = Add-VMHardDiskDrive -VM $VM -ControllerType SCSI -ControllerNumber 0 -ControllerLocation 0 -Path $VHDStoragePath -Passthru
	$VMDVDDrive = Add-VMDvdDrive -VM $VM -ControllerNumber 0 -ControllerLocation 1 -Passthru
	$VMNetAdapter = Get-VMNetworkAdapter -VM $VM
	Set-VMNetworkAdapter -VMNetworkAdapter $VMNetAdapter -StaticMacAddress ($VMNetAdapter.MacAddress)
	Set-VMFirmware -VM $VM -BootOrder $VMDVDDrive, $VMVHD, $VMNetAdapter -EnableSecureBoot On -SecureBootTemplate 'MicrosoftUEFICertificateAuthority'
	#Adding the ISO image to the vm
    Set-VMDvdDrive -VMDvdDrive $VMDVDDrive -Path $ISOPath

}
elseif ($OPT -eq "advance"){
    [string]$VMName = READ-HOST "What is the VM name?"
    $strRAM = READ-HOST "How much RAM do you want [ex: 2GB]?"
    $RAM = [int64]$strRAM.Replace('GB','') * 1GB
    $strHDSize = READ-HOST "How much HD do you want [ex: 10GB]?"
    [int64]$HDSize = [int64]$strHDSize.Replace('GB','') * 1GB
    $VHDXSizeBytes = $HDSize
    $MaximumMemory = $RAM
    $strProc = Read-Host "How man processess do you want? [Ex: 2]"
    [long]$Proc = [long]$strProc 
    
    
    $VM = New-VM -Name $VMName -MemoryStartupBytes $StartupMemory -SwitchName $VMSwitchName -Path $VMStoragePath -Generation 2 -NoVHD
	Set-VMMemory -VM $VM -DynamicMemoryEnabled $true -MinimumBytes $MinimumMemory -MaximumBytes $MaximumMemory
	Set-VMProcessor -VM $VM -Count 2
	Start-VM -VM $VM
	Stop-VM -VM $VM -Force
	New-VHD -Path $VHDStoragePath -SizeBytes $VHDXSizeBytes -Dynamic -BlockSizeBytes 1MB
	$VMVHD = Add-VMHardDiskDrive -VM $VM -ControllerType SCSI -ControllerNumber 0 -ControllerLocation 0 -Path $VHDStoragePath -Passthru
	$VMDVDDrive = Add-VMDvdDrive -VM $VM -ControllerNumber 0 -ControllerLocation 1 -Passthru
	$VMNetAdapter = Get-VMNetworkAdapter -VM $VM
	Set-VMNetworkAdapter -VMNetworkAdapter $VMNetAdapter -StaticMacAddress ($VMNetAdapter.MacAddress)
	Set-VMFirmware -VM $VM -BootOrder $VMDVDDrive, $VMVHD, $VMNetAdapter -EnableSecureBoot On -SecureBootTemplate 'MicrosoftUEFICertificateAuthority'
	#Adding the ISO image to the vm
    Set-VMDvdDrive -VMDvdDrive $VMDVDDrive -Path $ISOPath
} 
else{
    Write-Host "Unrecognized input... Try again!"
    break 
}

    
$ANS = READ-HOST "Whatchu wanna do? [Start <VMName>] [List [all] [running] ] [Remove <VMName>] [Rename <currName> <newName>] VM or [Quit]? "
while($ANS -ne "Quit"){
    $ANSList = -split $ANS
    $Count = $ANSList.Count
    [string ]$pram1 = $ANSList[0]
    [string ]$pram2 = $ANSList[1]
    [string ]$pram3 = $ANSList[2]


    if( $Count -ge 4){
        break
    }
    if ($pram1 -eq "Start") {

    #Start the VM
     START-VM -NAME $pram2 | out-host 
    
    }
    elseif ($pram1 -eq "Stop") {
        Stop-VM $pram2 | out-host 
    }

    elseif ($pram1 -eq "List") {
        
        if ($pram2 -eq "all") { 
            #Show all virtual machine on the server
            Get-VM | out-host 
        }
        elseif ($pram2 -eq "running") {
            #Show all virtual machine on the server running
             Get-VM | Where { $_.State –eq ‘Running’ } | out-host

        }
    }
    elseif ($pram1 -eq "Remove") {
            #Delete a VM of your choice
            $RVM = $pram2
            Stop-VM -Name $RVM 
            Remove-VM -Name $RVM -Force | out-host
            REMOVE-Item -Path C:\Users\Administrator\Desktop\VMs\$RVM\*.*   | out-host
     }
   

    elseif ($pram1 -eq "Rename") {
        #Extra Feature, renaming the VM
        
        [string]$OldName1 = $pram2
        [string]$NewName1 = $pram3
        Rename-VM -Name $OldName1 -NewName $NewName1 | out-host
    }
    else{
         Write-Host "Unrecognized input... Try again!"
    }
    $ANS = READ-HOST "Whatchu wanna do? [Start <VMName>] [Stop <VMName>] [Remove <VMName>] [List [all] [running] ]  [Rename <currName> <newName>] VM or [Quit]? "
}


