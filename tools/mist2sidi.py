#!/usr/bin/env python3

import sys

pin_assignment = {
        "SDRAM_A[0]"   : "PIN_B14",
        "SDRAM_A[1]"   : "PIN_C14",
        "SDRAM_A[2]"   : "PIN_C15",
        "SDRAM_A[3]"   : "PIN_C16",
        "SDRAM_A[4]"   : "PIN_B16",
        "SDRAM_A[5]"   : "PIN_A15",
        "SDRAM_A[6]"   : "PIN_A14",
        "SDRAM_A[7]"   : "PIN_A13",
        "SDRAM_A[8]"   : "PIN_A12",
        "SDRAM_A[9]"   : "PIN_D16",
        "SDRAM_A[10]"  : "PIN_B13",
        "SDRAM_A[11]"  : "PIN_D15",
        "SDRAM_A[12]"  : "PIN_D14",
        "SDRAM_BA[1]"  : "PIN_B12",
        "SDRAM_BA[0]"  : "PIN_A11",
        "SDRAM_CKE"    : "PIN_C11",
        "SDRAM_CLK"    : "PIN_R4",
        "SDRAM_DQ[15]" : "PIN_A2",
        "SDRAM_DQ[14]" : "PIN_A3",
        "SDRAM_DQ[13]" : "PIN_B3",
        "SDRAM_DQ[12]" : "PIN_A5",
        "SDRAM_DQ[11]" : "PIN_B5",
        "SDRAM_DQ[10]" : "PIN_B6",
        "SDRAM_DQ[9]"  : "PIN_C6",
        "SDRAM_DQ[8]"  : "PIN_E6",
        "SDRAM_DQ[7]"  : "PIN_B7",
        "SDRAM_DQ[6]"  : "PIN_A7",
        "SDRAM_DQ[5]"  : "PIN_D6",
        "SDRAM_DQ[4]"  : "PIN_A6",
        "SDRAM_DQ[3]"  : "PIN_B4",
        "SDRAM_DQ[2]"  : "PIN_A4",
        "SDRAM_DQ[1]"  : "PIN_C2",
        "SDRAM_DQ[0]"  : "PIN_C3",
        "SDRAM_DQMH"   : "PIN_C9",
        "SDRAM_DQML"   : "PIN_C8",
        "SDRAM_nCAS"   : "PIN_B10",
        "SDRAM_nCS"    : "PIN_B11",
        "SDRAM_nRAS"   : "PIN_A10",
        "SDRAM_nWE"    : "PIN_D8",
        "PIN_RX"       : "PIN_B1",
        "PIN_TX"       : "PIN_D1",
        "AUDIO_IN"     : "PIN_P1",
        "AUDIO_L"      : "PIN_T12",
        "AUDIO_R"      : "PIN_T13",
        "CLOCK_27"     : "PIN_E1",
        "CONF_DATA0"   : "PIN_H2",
        "LED"          : "PIN_G1",
        "SPI_DI"       : "PIN_R1",
        "SPI_DO"       : "PIN_T2",
        "SPI_SCK"      : "PIN_T3",
        "SPI_SS2"      : "PIN_T4",
        "SPI_SS3"      : "PIN_G15",
        "SPI_SS4"      : "PIN_G16",
        "VGA_B[5]"     : "PIN_J16",
        "VGA_B[4]"     : "PIN_J15",
        "VGA_B[3]"     : "PIN_J14",
        "VGA_B[2]"     : "PIN_K16",
        "VGA_B[1]"     : "PIN_K15",
        "VGA_B[0]"     : "PIN_J13",
        "VGA_G[5]"     : "PIN_F16",
        "VGA_G[4]"     : "PIN_F15",
        "VGA_G[3]"     : "PIN_L16",
        "VGA_G[2]"     : "PIN_L15",
        "VGA_G[1]"     : "PIN_N15",
        "VGA_G[0]"     : "PIN_N16",
        "VGA_R[5]"     : "PIN_P16",
        "VGA_R[4]"     : "PIN_P15",
        "VGA_R[3]"     : "PIN_R16",
        "VGA_R[2]"     : "PIN_R14",
        "VGA_R[1]"     : "PIN_T15",
        "VGA_R[0]"     : "PIN_T14",
        "VGA_VS"       : "PIN_T10",
        "VGA_HS"       : "PIN_T11"
        }


with open(sys.argv[1], 'r') as my_file:

    gbl_clk8 = 0
    gbl_clk64 = 0
    gbl_sdram_clk = 0
    gbl_spi_sck = 0
    gbl_clk32 = 0

    for line in my_file:
        line_updated = 0
        if "set_location_assignment" in line:
            tokens = line.split()
            if tokens[3] in pin_assignment:
                print("set_location_assignment " + pin_assignment[tokens[3]] + " -to " + tokens[3])
                line_updated = 1

        if line_updated == 0:
            print(line, end='')

        if "GLOBAL CLOCK" in line and "clk8" in line:
            gbl_clk8 = 1
        if "GLOBAL CLOCK" in line and "clk64" in line:
            gbl_clk64 = 1
        if "GLOBAL CLOCK" in line and "SDRAM_CLK" in line:
            gbl_sdram_clk = 1
        if "GLOBAL CLOCK" in line and "SPI_SCK" in line:
            gbl_spi_sck = 1
        if "GLOBAL CLOCK" in line and "clk32" in line:
            gbl_clk32 = 1

    print('')
    print('')
    if gbl_clk8 == 0:
        print("set_instance_assignment -name GLOBAL_SIGNAL \"GLOBAL CLOCK\" -to clk8")
    if gbl_clk64 == 0:
        print("set_instance_assignment -name GLOBAL_SIGNAL \"GLOBAL CLOCK\" -to clk64")
    if gbl_sdram_clk == 0:
        print("set_instance_assignment -name GLOBAL_SIGNAL \"GLOBAL CLOCK\" -to SDRAM_CLK")
    if gbl_spi_sck == 0:
        print("set_instance_assignment -name GLOBAL_SIGNAL \"GLOBAL CLOCK\" -to SPI_SCK")
    if gbl_clk32 == 0:
        print("set_instance_assignment -name GLOBAL_SIGNAL \"GLOBAL CLOCK\" -to clk32")
