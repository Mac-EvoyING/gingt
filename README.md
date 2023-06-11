# gingt
gingt is not a g-code terminal. 

Short tutorial:

- Connect your printer to the USB port

- Clone repository

- If you use windows, please change /dev/ttyUSB0 to the COM port where your printer is connected to.

- Open a terminal on the directory where gingt is located. If you have windows you can use cmd

- run the command:

python3 gingt.py


If everything went well, you should see messages like the following:

">>start
echo:Marlin 2.0.x
Marlin-AI3M 
echo: Last Updated: 2021-09-23 | Author: (knutwurst)
echo:Compiled: Sep 23 2021
echo: Free Memory: 1821  PlannerBufferBytes: 1568
echo:V76 stored settings retrieved (724 bytes; crc 36148)
echo:  G21    ; Units in mm (mm)
echo:; Filament settings: Disabled
echo:  M200 D1.75
echo:  M200 D0
echo:; Steps per unit:
echo: M92 X80.00 Y80.00 Z400.00 E393.00
echo:; Maximum feedrates (units/s):
echo:  M203 X500.00 Y500.00 Z6.00 E30.00
echo:; Maximum Acceleration (units/s2):
echo:  M201 X3000.00 Y2000.00 Z60.00 E10000.00
echo:; Acceleration (units/s2): P<print_accel> R<retract_accel> T<travel_accel>
echo:  M204 P1500.00 R1500.00 T3000.00
echo:; Advanced: B<min_segment_time_us> S<min_feedrate> T<min_travel_feedrate> X<max_x_jerk> Y<max_y_jerk> Z<max_z_jerk> E<max_e_jerk>
echo:  M205 B20000.00 S0.00 T0.00 X8.00 Y8.00 Z0.40 E5.00
echo:; Home offset:
echo:  M206 X0.00 Y0.00 Z0.00
echo:; Mesh Bed Leveling:
echo:  M420 S0 Z0.00
echo:; Endstop adjustment:
echo:  M666 Z0.00
echo:; PID settings:
echo:  M301 P12.78 I0.58 D70.90
echo:  M304 P251.78 I49.57 D319.73
echo:; Linear Advance:
echo:  M900 K0.00
echo:; Filament load/unload lengths:
echo:  M603 L538.00 U555.00
echo:SD init fail"

You can now test your printer capabilities, perform calibrations, PID Tuning, etc.
To exit just hit CTRL+C 2 times :D
