SET AqPallet=pallet_server.exe
SET AqPallet_PATH=Z:\Aqrose_Robot\Runit\AQPalletServer


PUSHD %AqPallet_PATH%
start cmd /C %AqPallet% %AqPallet% ^> out_console.txt
POPD
