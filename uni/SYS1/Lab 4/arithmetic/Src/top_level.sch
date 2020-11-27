<?xml version="1.0" encoding="UTF-8"?>
<drawing version="7">
    <attr value="zynq" name="DeviceFamilyName">
        <trait delete="all:0" />
        <trait editname="all:0" />
        <trait edittrait="all:0" />
    </attr>
    <netlist>
        <signal name="KEYPAD(7:0)" />
        <signal name="SWITCHES(6:0)" />
        <signal name="LED_RG(1:0)" />
        <signal name="LED_G(3:0)" />
        <signal name="LED_RGB(2:0)" />
        <signal name="SEL(2:0)" />
        <signal name="SEVEN_SEG(6:0)" />
        <signal name="CLK" />
        <signal name="RST" />
        <signal name="XLXN_149(6:0)" />
        <signal name="XLXN_150(6:0)" />
        <port polarity="BiDirectional" name="KEYPAD(7:0)" />
        <port polarity="Input" name="SWITCHES(6:0)" />
        <port polarity="Output" name="LED_RG(1:0)" />
        <port polarity="Output" name="LED_G(3:0)" />
        <port polarity="Output" name="LED_RGB(2:0)" />
        <port polarity="Output" name="SEL(2:0)" />
        <port polarity="Output" name="SEVEN_SEG(6:0)" />
        <port polarity="Input" name="CLK" />
        <port polarity="Input" name="RST" />
        <blockdef name="virtual_wires">
            <timestamp>2019-11-4T16:38:25</timestamp>
            <line x2="0" y1="-768" y2="-768" x1="64" />
            <line x2="0" y1="-704" y2="-704" x1="64" />
            <rect width="64" x="432" y="-780" height="24" />
            <line x2="496" y1="-768" y2="-768" x1="432" />
            <rect width="64" x="432" y="-332" height="24" />
            <line x2="496" y1="-320" y2="-320" x1="432" />
            <rect width="64" x="432" y="-268" height="24" />
            <line x2="496" y1="-256" y2="-256" x1="432" />
            <rect width="64" x="432" y="-572" height="24" />
            <line x2="496" y1="-560" y2="-560" x1="432" />
            <rect width="64" x="432" y="-508" height="24" />
            <line x2="496" y1="-496" y2="-496" x1="432" />
            <rect width="64" x="432" y="-444" height="24" />
            <line x2="496" y1="-432" y2="-432" x1="432" />
            <rect width="64" x="0" y="-556" height="24" />
            <line x2="64" y1="-544" y2="-544" x1="0" />
            <line x2="64" y1="-608" y2="-608" x1="0" />
            <line x2="432" y1="-688" y2="-688" x1="496" />
            <rect width="64" x="432" y="-700" height="24" />
            <rect width="64" x="0" y="-620" height="24" />
            <rect width="368" x="64" y="-796" height="988" />
            <line x2="0" y1="80" y2="80" x1="64" />
            <line x2="0" y1="144" y2="144" x1="64" />
            <rect width="64" x="0" y="-60" height="24" />
            <line x2="0" y1="-48" y2="-48" x1="64" />
            <rect width="64" x="0" y="4" height="24" />
            <line x2="0" y1="16" y2="16" x1="64" />
            <line x2="64" y1="-464" y2="-464" x1="0" />
            <line x2="64" y1="-400" y2="-400" x1="0" />
            <line x2="64" y1="-336" y2="-336" x1="0" />
        </blockdef>
        <blockdef name="constant">
            <timestamp>2006-1-1T10:10:10</timestamp>
            <rect width="112" x="0" y="0" height="64" />
            <line x2="112" y1="32" y2="32" x1="144" />
        </blockdef>
        <block symbolname="virtual_wires" name="XLXI_26">
            <blockpin signalname="CLK" name="CLK" />
            <blockpin signalname="RST" name="CLR" />
            <blockpin name="RED" />
            <blockpin name="GREEN" />
            <blockpin signalname="SWITCHES(6:0)" name="SWITCHES(6:0)" />
            <blockpin signalname="KEYPAD(7:0)" name="KEYPAD(7:0)" />
            <blockpin signalname="LED_RG(1:0)" name="LED_RG_o(1:0)" />
            <blockpin signalname="LED_G(3:0)" name="LED_G_o(3:0)" />
            <blockpin signalname="LED_RGB(2:0)" name="LED_RGB_o(2:0)" />
            <blockpin signalname="SEL(2:0)" name="SEL(2:0)" />
            <blockpin signalname="SEVEN_SEG(6:0)" name="SEVEN_SEG(6:0)" />
            <blockpin name="DIGIT_0(2:0)" />
            <blockpin name="DIGIT_1(2:0)" />
            <blockpin signalname="XLXN_150(6:0)" name="LED_0(6:0)" />
            <blockpin signalname="XLXN_149(6:0)" name="LED_1(6:0)" />
            <blockpin name="SW_0" />
            <blockpin name="SW_1" />
            <blockpin name="SW_2" />
        </block>
        <block symbolname="constant" name="XLXI_29">
            <attr value="FF" name="CValue">
                <trait delete="all:1 sym:0" />
                <trait editname="all:1 sch:0" />
                <trait valuetype="BitVector 32 Hexadecimal" />
            </attr>
            <blockpin signalname="XLXN_149(6:0)" name="O" />
        </block>
        <block symbolname="constant" name="XLXI_28">
            <attr value="FF" name="CValue">
                <trait delete="all:1 sym:0" />
                <trait editname="all:1 sch:0" />
                <trait valuetype="BitVector 32 Hexadecimal" />
            </attr>
            <blockpin signalname="XLXN_150(6:0)" name="O" />
        </block>
    </netlist>
    <sheet sheetnum="1" width="2720" height="1760">
        <instance x="1440" y="1184" name="XLXI_26" orien="R0">
        </instance>
        <branch name="KEYPAD(7:0)">
            <wire x2="2016" y1="416" y2="416" x1="1936" />
        </branch>
        <branch name="SWITCHES(6:0)">
            <wire x2="2016" y1="496" y2="496" x1="1936" />
        </branch>
        <branch name="LED_RG(1:0)">
            <wire x2="2000" y1="624" y2="624" x1="1936" />
        </branch>
        <branch name="LED_G(3:0)">
            <wire x2="2000" y1="688" y2="688" x1="1936" />
        </branch>
        <branch name="LED_RGB(2:0)">
            <wire x2="2000" y1="752" y2="752" x1="1936" />
        </branch>
        <branch name="SEL(2:0)">
            <wire x2="2000" y1="864" y2="864" x1="1936" />
        </branch>
        <branch name="SEVEN_SEG(6:0)">
            <wire x2="2000" y1="928" y2="928" x1="1936" />
        </branch>
        <branch name="CLK">
            <wire x2="1440" y1="416" y2="416" x1="1280" />
        </branch>
        <branch name="RST">
            <wire x2="1440" y1="480" y2="480" x1="1280" />
        </branch>
        <instance x="1232" y="1168" name="XLXI_29" orien="R0">
        </instance>
        <instance x="1232" y="1056" name="XLXI_28" orien="R0">
        </instance>
        <branch name="XLXN_149(6:0)">
            <wire x2="1440" y1="1200" y2="1200" x1="1376" />
        </branch>
        <branch name="XLXN_150(6:0)">
            <wire x2="1408" y1="1088" y2="1088" x1="1376" />
            <wire x2="1408" y1="1088" y2="1136" x1="1408" />
            <wire x2="1440" y1="1136" y2="1136" x1="1408" />
        </branch>
        <iomarker fontsize="28" x="2016" y="416" name="KEYPAD(7:0)" orien="R0" />
        <iomarker fontsize="28" x="2016" y="496" name="SWITCHES(6:0)" orien="R0" />
        <iomarker fontsize="28" x="2000" y="624" name="LED_RG(1:0)" orien="R0" />
        <iomarker fontsize="28" x="2000" y="688" name="LED_G(3:0)" orien="R0" />
        <iomarker fontsize="28" x="2000" y="752" name="LED_RGB(2:0)" orien="R0" />
        <iomarker fontsize="28" x="2000" y="864" name="SEL(2:0)" orien="R0" />
        <iomarker fontsize="28" x="2000" y="928" name="SEVEN_SEG(6:0)" orien="R0" />
        <iomarker fontsize="28" x="1280" y="416" name="CLK" orien="R180" />
        <iomarker fontsize="28" x="1280" y="480" name="RST" orien="R180" />
    </sheet>
</drawing>