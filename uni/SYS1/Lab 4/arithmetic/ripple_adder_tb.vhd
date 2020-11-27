
LIBRARY ieee;
USE ieee.std_logic_1164.ALL;

ENTITY ripple_adder_tb IS
END ripple_adder_tb;
ARCHITECTURE behavioral OF ripple_adder_tb IS 

   COMPONENT ripple_adder
   PORT( 
	  CIN	 :	IN	STD_LOGIC; 
     COUT :	OUT	STD_LOGIC; 
     A	 :	IN	STD_LOGIC_VECTOR (2 DOWNTO 0); 
     B	 :	IN	STD_LOGIC_VECTOR (2 DOWNTO 0); 
     SUM	 :	OUT	STD_LOGIC_VECTOR (2 DOWNTO 0));
   END COMPONENT;

   SIGNAL CIN	:	STD_LOGIC;
   SIGNAL COUT	:	STD_LOGIC;
   SIGNAL A	:	STD_LOGIC_VECTOR (2 DOWNTO 0);
   SIGNAL B	:	STD_LOGIC_VECTOR (2 DOWNTO 0);
   SIGNAL SUM	:	STD_LOGIC_VECTOR (2 DOWNTO 0);

BEGIN

   UUT: ripple_adder PORT MAP(
		CIN => CIN, 
		COUT => COUT, 
		A => A, 
		B => B, 
		SUM => SUM
   );

-- *** Test Bench - User Defined Section ***
   tb : PROCESS
   BEGIN
	   CIN <= '0'; B <= "000"; A <= "000"; WAIT FOR 100 ns;
	   CIN <= '0'; B <= "000"; A <= "001"; WAIT FOR 100 ns;		
	   CIN <= '0'; B <= "000"; A <= "010"; WAIT FOR 100 ns;
	   CIN <= '0'; B <= "000"; A <= "100"; WAIT FOR 100 ns;
	   CIN <= '0'; B <= "001"; A <= "001"; WAIT FOR 100 ns;		
	   CIN <= '0'; B <= "010"; A <= "010"; WAIT FOR 100 ns;
	   CIN <= '0'; B <= "100"; A <= "100"; WAIT FOR 100 ns;	
	   CIN <= '1'; B <= "001"; A <= "001"; WAIT FOR 100 ns;		
	   CIN <= '1'; B <= "010"; A <= "010"; WAIT FOR 100 ns;
	   CIN <= '1'; B <= "100"; A <= "100"; WAIT FOR 100 ns;				
      WAIT; -- will wait forever
   END PROCESS;
-- *** End Test Bench - User Defined Section ***

END;
