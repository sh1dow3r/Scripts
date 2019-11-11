#How many vms you want to create
[uint16]$VMS = READ-HOST "How many VMs do you want?"

#Switch Will be used for the VM
$VMSwitch = Get-VMSwitch | Select-Object name

#The path used for the vms
$VMPath = "E:\Demo\VMs"

#ISO path for the VMS
$ISOPath = "C:\Users\Administrator\Desktop\CentOS-7-x86_64-Minimal-1810.iso"

#For loop instintiate a VM and set the default variables
FOR ($VM=1; $VM -le $VMS ;$VM++){
    $OPT = READ-HOST "Do you want a [basic] or [advance] VM?"
    $NAME = READ-HOST "What is the VM name?"
    if ($OPT -eq "basic") {
    NEW-VM -NAME $NAME `
           -PATH E:\Demo\VMs `
           -NEWVHDPath "e:\Demo\VMs\$name.vhdx" `
           -NewVHDSizeBytes 10GB `
           -MemoryStartupBytes 2GB `
           -SwitchName $VMSwitch `
            -Generation 1 `
            -BootDevice CD
    }
    if ($OPT -eq "advance"){
    [int64]$RAM = READ-HOST "How much RAM do you want [ex: 2GB]?"
    [int64]$VHDX = READ-HOST "How much HD do you want [ex: 10GB]?"
     NEW-VM -NAME $NAME `
           -PATH E:\Demo\VMs `
           -NEWVHDPath "e:\Demo\VMs\$name.vhdx" `
           -NewVHDSizeBytes $VHDX `
           -MemoryStartupBytes $RAM `
           -SwitchName $VMSwitch `
            -Generation 1 `
            -BootDevice CD
    
    
    } 
    SET-VM -NAME $NAME -PROCESSORCOUNT 2
    
    #Adding the ISO image to the vm
    Add-VMDvdDrive -VMName $NAME -PATH $ISOPath

    while($true)
    {
        $ANS = READ-HOST "Whatchu wanna do? [Start <VMName>] [List [all] [running]] [Remove <VMName>] VM? "
        #Start the VM

        START-VM -NAME $NAME

        #Show all virtual machine on the server
        Get-VM 

        #Show all virtual machine on the server running
        Get-VM | Where { $_.State –eq ‘Running’ }

        #Delete a VM of your choice
        REA

        #Extra Feature, renaming the VM
        $RENAME = READ-HOST "Do you happen to want to rename the VM? [Y] Yes"
        if($RENAME -eq "Y"){
        $NName = READ-HOST "What is the new name?"
        Rename-VM -Name $NAME -NewName $NName
        }
        #Removing a VM
        $RENAME = READ-HOST "Do you want to remove a VM? [Y] Yes"
        if($RENAME -eq "Y"){
        $RName = READ-HOST "What is the name of the VM you want to remove?"
        Rename-VM -Name $RNAME -Force
        REMOVE-Item -Path E:\Demo\VMS\*.*  
    }
}

    