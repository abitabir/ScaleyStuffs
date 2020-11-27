
LIBRARY ieee;
USE ieee.std_logic_1164.ALL;

ENTITY full_adder_tb IS
END full_adder_tb;
ARCHITECTURE behavioral OF full_adder_tb IS 

   COMPONENT full_adder
   PORT( 
	  A	:	IN	STD_LOGIC; 
     B	:	IN	STD_LOGIC; 
     CIN	:	IN	STD_LOGIC; 
     COUT:	OUT	STD_LOGIC; 
     SUM	:	OUT	STD_LOGIC);
   END COMPONENT;

   SIGNAL A	:	STD_LOGIC;
   SIGNAL B	:	STD_LOGIC;
   SIGNAL CIN	:	STD_LOGIC;
   SIGNAL COUT	:	STD_LOGIC;
   SIGNAL SUM	:	STD_LOGIC;

BEGIN

   UUT: full_adder PORT MAP(
		A => A, 
		B => B, 
		CIN => CIN, 
		COUT => COUT, 
		SUM => SUM
   );

-- *** Test Bench - User Defined Section ***
   tb : PROCESS
   BEGIN
	   A <= '0'; B <= '0'; CIN <= '0'; WAIT FOR 100 ns;
	   A <= '0'; B <= '1'; CIN <= '0'; WAIT FOR 100 ns;
	   A <= '1'; B <= '0'; CIN <= '0'; WAIT FOR 100 ns;
	   A <= '1'; B <= '1'; CIN <= '0'; WAIT FOR 100 ns;
	   A <= '0'; B <= '0'; CIN <= '1'; WAIT FOR 100 ns;
	   A <= '0'; B <= '1'; CIN <= '1'; WAIT FOR 100 ns;
	   A <= '1'; B <= '0'; CIN <= '1'; WAIT FOR 100 ns;
	   A <= '1'; B <= '1'; CIN <= '1'; WAIT FOR 100 ns;		
      WAIT; -- will wait forever
   END PROCESS;
-- *** End Test Bench - User Defined Section ***

END;
