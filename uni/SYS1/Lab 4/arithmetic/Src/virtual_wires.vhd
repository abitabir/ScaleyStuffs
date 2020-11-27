-- =============================================================================================================
-- *
-- * Copyright (c) M.Freeman
-- *
-- * File Name: virtual_wires.vhd
-- *
-- * Version: V1.0
-- *
-- * Release Date:
-- *
-- * Author(s): M.Freeman
-- *
-- * Description: Single core PicoBlaze top level virtual wires 
-- *
-- * Change History:  $Author: $
-- *                  $Date: $
-- *                  $Revision: $
-- *
-- * Conditions of Use: THIS CODE IS COPYRIGHT AND IS SUPPLIED "AS IS" WITHOUT WARRANTY OF ANY KIND, INCLUDING,
-- *                    BUT NOT LIMITED TO, ANY IMPLIED WARRANTY OF MERCHANTABILITY AND FITNESS FOR A
-- *                    PARTICULAR PURPOSE.
-- *
-- * Notes:
-- *
-- =============================================================================================================

LIBRARY IEEE;
USE IEEE.STD_LOGIC_1164.ALL; 
USE IEEE.std_logic_arith.ALL;

LIBRARY UNISIM;
USE UNISIM.vcomponents.ALL;

ENTITY virtual_wires IS
PORT (
  CLK       : IN  STD_LOGIC;
  CLR       : IN  STD_LOGIC; 
  
  RED       : IN  STD_LOGIC; 
  GREEN     : IN  STD_LOGIC; 

  LED_0     : IN STD_LOGIC_VECTOR(6 DOWNTO 0);   
  LED_1     : IN STD_LOGIC_VECTOR(6 DOWNTO 0);    
  
  SWITCHES  : IN STD_LOGIC_VECTOR(6 DOWNTO 0);
  
  LED_RG_o  : OUT STD_LOGIC_VECTOR(1 DOWNTO 0);
  LED_G_o   : OUT STD_LOGIC_VECTOR(3 DOWNTO 0);
  LED_RGB_o : OUT STD_LOGIC_VECTOR(2 DOWNTO 0);  
  
  SEL       : OUT STD_LOGIC_VECTOR(2 DOWNTO 0); 
  SEVEN_SEG : OUT STD_LOGIC_VECTOR(6 DOWNTO 0); 
  
  DIGIT_0   : OUT STD_LOGIC_VECTOR(2 DOWNTO 0);
  DIGIT_1   : OUT STD_LOGIC_VECTOR(2 DOWNTO 0); 
  
  SW_0      : OUT STD_LOGIC; 
  SW_1      : OUT STD_LOGIC;  
  SW_2      : OUT STD_LOGIC; 
  
  KEYPAD    : INOUT STD_LOGIC_VECTOR(7 DOWNTO 0)    ); 
  
END virtual_wires;

ARCHITECTURE virtual_wires_arch OF virtual_wires IS

  -- ##############
  -- # Components #
  -- ##############

  --
  -- Processor
  --

  COMPONENT picoblze_top_level IS
  PORT (
    clk_i      : IN  STD_LOGIC;
    rst_i      : IN  STD_LOGIC;  
  
    pio_A_o    : OUT  STD_LOGIC_VECTOR(6 DOWNTO 0);
    pio_B_o    : OUT STD_LOGIC_VECTOR(5 DOWNTO 0);

    pio_C_A_i  : IN  STD_LOGIC_VECTOR(6 DOWNTO 0);
    pio_C_B_i  : IN  STD_LOGIC_VECTOR(6 DOWNTO 0);
    pio_C_C_i  : IN  STD_LOGIC_VECTOR(6 DOWNTO 0);
    pio_C_D_i  : IN  STD_LOGIC_VECTOR(6 DOWNTO 0);
	 
    pio_D_dir  : OUT STD_LOGIC_VECTOR(7 DOWNTO 0); 
    pio_D_i    : IN  STD_LOGIC_VECTOR(7 DOWNTO 0);
    pio_D_o    : OUT STD_LOGIC_VECTOR(7 DOWNTO 0);

    pio_E_i    : IN  STD_LOGIC_VECTOR(6 DOWNTO 0);
    pio_E_o    : OUT STD_LOGIC_VECTOR(5 DOWNTO 0);

    pio_F_i    : IN  STD_LOGIC_VECTOR(1 DOWNTO 0);
    pio_F_o    : OUT STD_LOGIC_VECTOR(5 DOWNTO 0);

    pio_G_o    : OUT STD_LOGIC_VECTOR(2 DOWNTO 0) ); 
  END COMPONENT;

  -- ###########
  -- # Signals #
  -- ###########

  SIGNAL GND        : STD_LOGIC;
  SIGNAL VCC        : STD_LOGIC;
  SIGNAL GND_BUS    : STD_LOGIC_VECTOR(7 DOWNTO 0);
  SIGNAL BLANK      : STD_LOGIC_VECTOR(6 DOWNTO 0);  

  SIGNAL  pio_B_int : STD_LOGIC_VECTOR(5 DOWNTO 0);
  
  SIGNAL  pio_D_int : STD_LOGIC_VECTOR(7 DOWNTO 0);
  SIGNAL  pio_D_dir : STD_LOGIC_VECTOR(7 DOWNTO 0);
  
  SIGNAL  pio_E_int : STD_LOGIC_VECTOR(5 DOWNTO 0);
  
  SIGNAL  pio_F_o_int : STD_LOGIC_VECTOR(5 DOWNTO 0);  
  SIGNAL  pio_F_i_int : STD_LOGIC_VECTOR(1 DOWNTO 0);  
  
  SIGNAL  pio_G_int : STD_LOGIC_VECTOR(2 DOWNTO 0);  
  
BEGIN

  --
  -- SIGNAL BUFFERS
  --

  GND     <= '0';
  VCC     <= '1';
  GND_BUS <= "00000000";
  BLANK   <= "0000000"; 
  
  SEL       <= pio_B_int(2 DOWNTO 0);
  LED_RGB_o <= pio_B_int(5 DOWNTO 3); 
 
  LED_G_o   <= pio_E_int(3 DOWNTO 0); 
  LED_RG_o  <= pio_E_int(5 DOWNTO 4);
  
  DIGIT_0   <= pio_F_o_int(2 DOWNTO 0); 
  DIGIT_1   <= pio_F_o_int(5 DOWNTO 3);  

  KEYPAD(0) <=  pio_D_int(0) WHEN (pio_D_dir(0) = '1') ELSE 'Z';
  KEYPAD(1) <=  pio_D_int(1) WHEN (pio_D_dir(1) = '1') ELSE 'Z';
  KEYPAD(2) <=  pio_D_int(2) WHEN (pio_D_dir(2) = '1') ELSE 'Z';
  KEYPAD(3) <=  pio_D_int(3) WHEN (pio_D_dir(3) = '1') ELSE 'Z';
  
  KEYPAD(4) <=  pio_D_int(4) WHEN (pio_D_dir(4) = '1') ELSE 'Z';
  KEYPAD(5) <=  pio_D_int(5) WHEN (pio_D_dir(5) = '1') ELSE 'Z';
  KEYPAD(6) <=  pio_D_int(6) WHEN (pio_D_dir(6) = '1') ELSE 'Z';
  KEYPAD(7) <=  pio_D_int(7) WHEN (pio_D_dir(7) = '1') ELSE 'Z';
  
  pio_F_i_int <= RED & GREEN;
  
  SW_0 <= pio_G_int(0);
  SW_1 <= pio_G_int(1); 
  SW_2 <= pio_G_int(2); 
  
  -- ##############
  -- # Components #
  -- ##############

  vw : picoblze_top_level PORT MAP(
    clk_i     => CLK,
    rst_i     => CLR,
    pio_A_o   => SEVEN_SEG ,  
    pio_B_o   => pio_B_int,    
    pio_C_A_i => LED_0,    
    pio_C_B_i => LED_1,     
    pio_C_C_i => BLANK,      
    pio_C_D_i => BLANK,     	 
    pio_D_dir => pio_D_dir,    
    pio_D_i   => KEYPAD,      
    pio_D_o   => pio_D_int,      
    pio_E_i   => SWITCHES,
    pio_E_o   => pio_E_int,
    pio_F_i   => pio_F_i_int,
    pio_F_o   => pio_F_o_int, 
    pio_G_o   => pio_G_int ); 

END virtual_wires_arch;
