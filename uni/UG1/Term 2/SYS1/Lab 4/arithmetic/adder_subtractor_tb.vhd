
LIBRARY ieee;
USE ieee.std_logic_1164.ALL;

ENTITY adder_subtractor_tb IS
END adder_subtractor_tb;
ARCHITECTURE behavioral OF adder_subtractor_tb IS 

   COMPONENT ripple_adder
   PORT( 
	  CIN	:	IN	 STD_LOGIC; 
     COUT:	OUT STD_LOGIC; 
     A	:	IN	 STD_LOGIC_VECTOR (2 DOWNTO 0); 
     B	:	IN	 STD_LOGIC_VECTOR (2 DOWNTO 0); 
     SUM	:	OUT STD_LOGIC_VECTOR (2 DOWNTO 0));
   END COMPONENT;
	
   COMPONENT mux2_3
   PORT( 
     A   : IN	STD_LOGIC_VECTOR (2 DOWNTO 0); 
     B   : IN	STD_LOGIC_VECTOR (2 DOWNTO 0); 
     Y   : OUT STD_LOGIC_VECTOR (2 DOWNTO 0);
	  SEL : IN STD_LOGIC );
   END COMPONENT;
	
   COMPONENT inv3
   PORT( 
     A   : IN	STD_LOGIC_VECTOR (2 DOWNTO 0); 
     Y   : OUT STD_LOGIC_VECTOR (2 DOWNTO 0) );
   END COMPONENT;

   SIGNAL CIN	 :	STD_LOGIC;
   SIGNAL COUT	 :	STD_LOGIC;
   SIGNAL A	    :	STD_LOGIC_VECTOR (2 DOWNTO 0);
   SIGNAL B	    :	STD_LOGIC_VECTOR (2 DOWNTO 0);
   SIGNAL NOT_B :	STD_LOGIC_VECTOR (2 DOWNTO 0);
   SIGNAL B_OUT :	STD_LOGIC_VECTOR (2 DOWNTO 0);	
   SIGNAL SUM	 :	STD_LOGIC_VECTOR (2 DOWNTO 0);

BEGIN

   adder: ripple_adder PORT MAP(
		CIN  => CIN, 
		COUT => COUT, 
		A    => A, 
		B    => B_OUT, 
		SUM  => SUM
   );
	
   mux: mux2_3 PORT MAP( 
     A   => B, 
     B   => NOT_B,
     Y   => B_OUT,
	  SEL => CIN);
	
   invert: inv3 PORT MAP(  
     A => B,
     Y => NOT_B );
	
   -- *** Test Bench - User Defined Section ***
   tb : PROCESS
   BEGIN
	   CIN <= '0'; A <= "000"; B <= "000"; WAIT FOR 100 ns;
	   CIN <= '0'; A <= "010"; B <= "001"; WAIT FOR 100 ns;
	   CIN <= '0'; A <= "100"; B <= "010"; WAIT FOR 100 ns;
	   CIN <= '1'; A <= "000"; B <= "000"; WAIT FOR 100 ns;
	   CIN <= '1'; A <= "010"; B <= "001"; WAIT FOR 100 ns;
	   CIN <= '1'; A <= "100"; B <= "010"; WAIT FOR 100 ns;
	   CIN <= '1'; A <= "010"; B <= "100"; WAIT FOR 100 ns;	
	   CIN <= '0'; A <= "000"; B <= "000"; WAIT FOR 100 ns;		
      WAIT; -- will wait forever
   END PROCESS;
   -- *** End Test Bench - User Defined Section ***

END;
