
LIBRARY ieee;
USE ieee.std_logic_1164.ALL;

ENTITY multiplier_tb IS
END multiplier_tb;
ARCHITECTURE behavioral OF multiplier_tb IS 

   COMPONENT multiplier
   PORT( A	:	IN	STD_LOGIC_VECTOR (2 DOWNTO 0); 
         B	:	IN	STD_LOGIC_VECTOR (2 DOWNTO 0); 
         Y	:	OUT	STD_LOGIC_VECTOR (5 DOWNTO 0));
   END COMPONENT;

   SIGNAL A	:	STD_LOGIC_VECTOR (2 DOWNTO 0);
   SIGNAL B	:	STD_LOGIC_VECTOR (2 DOWNTO 0);
   SIGNAL Y	:	STD_LOGIC_VECTOR (5 DOWNTO 0);

BEGIN

   UUT: multiplier PORT MAP(
		A => A, 
		B => B, 
		Y => Y
   );

-- *** Test Bench - User Defined Section ***
   tb : PROCESS
   BEGIN
	   A <= "000"; B <= "001"; WAIT FOR 100ns;
	   A <= "001"; B <= "000"; WAIT FOR 100ns;		
	   A <= "010"; B <= "010"; WAIT FOR 100ns;
	   A <= "101"; B <= "101"; WAIT FOR 100ns;
	   A <= "111"; B <= "001"; WAIT FOR 100ns;		
	   A <= "111"; B <= "010"; WAIT FOR 100ns;
	   A <= "111"; B <= "011"; WAIT FOR 100ns;		
	   A <= "111"; B <= "100"; WAIT FOR 100ns;
	   A <= "111"; B <= "101"; WAIT FOR 100ns;
	   A <= "111"; B <= "110"; WAIT FOR 100ns;	
	   A <= "111"; B <= "111"; WAIT FOR 100ns;

      WAIT; -- will wait forever
   END PROCESS;
-- *** End Test Bench - User Defined Section ***

END;
