#!/bin/bash

# Clean the install folder
# Push all the code from code folder to Install folder

chmod 700 *
InstallerFolder=ElectionSimulationInstaller
rm -rf ../${InstallerFolder}/ElectionSimulation/
mkdir ../${InstallerFolder}/ElectionSimulation/
cp -r ./ElectionSimulation/ ../${InstallerFolder}
tar -zcvf ../ElectionSimulation.tgz ../ElectionSimulationInstaller