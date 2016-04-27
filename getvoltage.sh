#!/bin/bash

COREV=$(/opt/vc/bin/vcgencmd measure_volts core)
SDRAMCOREV=$(/opt/vc/bin/vcgencmd measure_volts sdram_c)
SDRAMIOV=$(/opt/vc/bin/vcgencmd measure_volts sdram_i)
SDRAMPV=$(/opt/vc/bin/vcgencmd measure_volts sdram_p)

echo "Core voltage: $COREV"
echo "SDRAM Core voltage: $SDRAMCOREV"
echo "SDRAM IO voltage: $SDRAMIOV"
echo "SDRAM PHY voltage: $SDRAMPV"


