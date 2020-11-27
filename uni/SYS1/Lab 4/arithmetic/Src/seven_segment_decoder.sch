<?xml version="1.0" encoding="UTF-8"?>
<drawing version="7">
    <attr value="zynq" name="DeviceFamilyName">
        <trait delete="all:0" />
        <trait editname="all:0" />
        <trait edittrait="all:0" />
    </attr>
    <netlist>
        <signal name="Y7" />
        <signal name="Y6" />
        <signal name="Y4" />
        <signal name="Y3" />
        <signal name="Y2" />
        <signal name="Y1" />
        <signal name="Y0" />
        <signal name="Y5" />
        <signal name="A" />
        <signal name="B" />
        <signal name="C" />
        <signal name="D" />
        <signal name="E" />
        <signal name="F" />
        <signal name="G" />
        <port polarity="Input" name="Y7" />
        <port polarity="Input" name="Y6" />
        <port polarity="Input" name="Y4" />
        <port polarity="Input" name="Y3" />
        <port polarity="Input" name="Y2" />
        <port polarity="Input" name="Y1" />
        <port polarity="Input" name="Y0" />
        <port polarity="Input" name="Y5" />
        <port polarity="Output" name="A" />
        <port polarity="Output" name="B" />
        <port polarity="Output" name="C" />
        <port polarity="Output" name="D" />
        <port polarity="Output" name="E" />
        <port polarity="Output" name="F" />
        <port polarity="Output" name="G" />
        <blockdef name="or2">
            <timestamp>2000-1-1T10:10:10</timestamp>
            <line x2="64" y1="-64" y2="-64" x1="0" />
            <line x2="64" y1="-128" y2="-128" x1="0" />
            <line x2="192" y1="-96" y2="-96" x1="256" />
            <arc ex="192" ey="-96" sx="112" sy="-48" r="88" cx="116" cy="-136" />
            <arc ex="48" ey="-144" sx="48" sy="-48" r="56" cx="16" cy="-96" />
            <line x2="48" y1="-144" y2="-144" x1="112" />
            <arc ex="112" ey="-144" sx="192" sy="-96" r="88" cx="116" cy="-56" />
            <line x2="48" y1="-48" y2="-48" x1="112" />
        </blockdef>
        <blockdef name="buf">
            <timestamp>2000-1-1T10:10:10</timestamp>
            <line x2="64" y1="-32" y2="-32" x1="0" />
            <line x2="128" y1="-32" y2="-32" x1="224" />
            <line x2="128" y1="0" y2="-32" x1="64" />
            <line x2="64" y1="-32" y2="-64" x1="128" />
            <line x2="64" y1="-64" y2="0" x1="64" />
        </blockdef>
        <blockdef name="or3">
            <timestamp>2000-1-1T10:10:10</timestamp>
            <line x2="48" y1="-64" y2="-64" x1="0" />
            <line x2="72" y1="-128" y2="-128" x1="0" />
            <line x2="48" y1="-192" y2="-192" x1="0" />
            <line x2="192" y1="-128" y2="-128" x1="256" />
            <arc ex="192" ey="-128" sx="112" sy="-80" r="88" cx="116" cy="-168" />
            <arc ex="48" ey="-176" sx="48" sy="-80" r="56" cx="16" cy="-128" />
            <line x2="48" y1="-64" y2="-80" x1="48" />
            <line x2="48" y1="-192" y2="-176" x1="48" />
            <line x2="48" y1="-80" y2="-80" x1="112" />
            <arc ex="112" ey="-176" sx="192" sy="-128" r="88" cx="116" cy="-88" />
            <line x2="48" y1="-176" y2="-176" x1="112" />
        </blockdef>
        <blockdef name="or5">
            <timestamp>2000-1-1T10:10:10</timestamp>
            <line x2="48" y1="-64" y2="-64" x1="0" />
            <line x2="48" y1="-128" y2="-128" x1="0" />
            <line x2="72" y1="-192" y2="-192" x1="0" />
            <line x2="48" y1="-256" y2="-256" x1="0" />
            <line x2="48" y1="-320" y2="-320" x1="0" />
            <line x2="192" y1="-192" y2="-192" x1="256" />
            <arc ex="192" ey="-192" sx="112" sy="-144" r="88" cx="116" cy="-232" />
            <line x2="48" y1="-240" y2="-240" x1="112" />
            <line x2="48" y1="-144" y2="-144" x1="112" />
            <line x2="48" y1="-64" y2="-144" x1="48" />
            <line x2="48" y1="-320" y2="-240" x1="48" />
            <arc ex="112" ey="-240" sx="192" sy="-192" r="88" cx="116" cy="-152" />
            <arc ex="48" ey="-240" sx="48" sy="-144" r="56" cx="16" cy="-192" />
        </blockdef>
        <blockdef name="or4">
            <timestamp>2000-1-1T10:10:10</timestamp>
            <line x2="48" y1="-64" y2="-64" x1="0" />
            <line x2="64" y1="-128" y2="-128" x1="0" />
            <line x2="64" y1="-192" y2="-192" x1="0" />
            <line x2="48" y1="-256" y2="-256" x1="0" />
            <line x2="192" y1="-160" y2="-160" x1="256" />
            <arc ex="112" ey="-208" sx="192" sy="-160" r="88" cx="116" cy="-120" />
            <line x2="48" y1="-208" y2="-208" x1="112" />
            <line x2="48" y1="-112" y2="-112" x1="112" />
            <line x2="48" y1="-256" y2="-208" x1="48" />
            <line x2="48" y1="-64" y2="-112" x1="48" />
            <arc ex="48" ey="-208" sx="48" sy="-112" r="56" cx="16" cy="-160" />
            <arc ex="192" ey="-160" sx="112" sy="-112" r="88" cx="116" cy="-200" />
        </blockdef>
        <block symbolname="or2" name="XLXI_1">
            <blockpin signalname="Y1" name="I0" />
            <blockpin signalname="Y4" name="I1" />
            <blockpin signalname="A" name="O" />
        </block>
        <block symbolname="or2" name="XLXI_2">
            <blockpin signalname="Y6" name="I0" />
            <blockpin signalname="Y5" name="I1" />
            <blockpin signalname="B" name="O" />
        </block>
        <block symbolname="buf" name="XLXI_3">
            <blockpin signalname="Y2" name="I" />
            <blockpin signalname="C" name="O" />
        </block>
        <block symbolname="or3" name="XLXI_4">
            <blockpin signalname="Y1" name="I0" />
            <blockpin signalname="Y4" name="I1" />
            <blockpin signalname="Y7" name="I2" />
            <blockpin signalname="D" name="O" />
        </block>
        <block symbolname="or5" name="XLXI_5">
            <blockpin signalname="Y1" name="I0" />
            <blockpin signalname="Y3" name="I1" />
            <blockpin signalname="Y4" name="I2" />
            <blockpin signalname="Y5" name="I3" />
            <blockpin signalname="Y7" name="I4" />
            <blockpin signalname="E" name="O" />
        </block>
        <block symbolname="or4" name="XLXI_6">
            <blockpin signalname="Y1" name="I0" />
            <blockpin signalname="Y2" name="I1" />
            <blockpin signalname="Y3" name="I2" />
            <blockpin signalname="Y7" name="I3" />
            <blockpin signalname="F" name="O" />
        </block>
        <block symbolname="or3" name="XLXI_7">
            <blockpin signalname="Y0" name="I0" />
            <blockpin signalname="Y1" name="I1" />
            <blockpin signalname="Y7" name="I2" />
            <blockpin signalname="G" name="O" />
        </block>
    </netlist>
    <sheet sheetnum="1" width="2720" height="1760">
        <branch name="Y7">
            <wire x2="1120" y1="96" y2="96" x1="720" />
            <wire x2="1120" y1="96" y2="688" x1="1120" />
            <wire x2="1280" y1="688" y2="688" x1="1120" />
            <wire x2="1120" y1="688" y2="880" x1="1120" />
            <wire x2="1296" y1="880" y2="880" x1="1120" />
            <wire x2="1120" y1="880" y2="1200" x1="1120" />
            <wire x2="1296" y1="1200" y2="1200" x1="1120" />
            <wire x2="1120" y1="1200" y2="1456" x1="1120" />
            <wire x2="1120" y1="1456" y2="1616" x1="1120" />
            <wire x2="1296" y1="1456" y2="1456" x1="1120" />
        </branch>
        <branch name="Y6">
            <wire x2="1072" y1="144" y2="144" x1="720" />
            <wire x2="1072" y1="144" y2="528" x1="1072" />
            <wire x2="1264" y1="528" y2="528" x1="1072" />
            <wire x2="1072" y1="528" y2="1616" x1="1072" />
        </branch>
        <branch name="Y4">
            <wire x2="976" y1="240" y2="240" x1="720" />
            <wire x2="976" y1="240" y2="320" x1="976" />
            <wire x2="1280" y1="320" y2="320" x1="976" />
            <wire x2="976" y1="320" y2="744" x1="976" />
            <wire x2="976" y1="744" y2="752" x1="976" />
            <wire x2="1280" y1="752" y2="752" x1="976" />
            <wire x2="976" y1="752" y2="1008" x1="976" />
            <wire x2="1296" y1="1008" y2="1008" x1="976" />
            <wire x2="976" y1="1008" y2="1616" x1="976" />
        </branch>
        <branch name="Y3">
            <wire x2="928" y1="288" y2="288" x1="720" />
            <wire x2="928" y1="288" y2="1072" x1="928" />
            <wire x2="1296" y1="1072" y2="1072" x1="928" />
            <wire x2="928" y1="1072" y2="1264" x1="928" />
            <wire x2="928" y1="1264" y2="1616" x1="928" />
            <wire x2="1296" y1="1264" y2="1264" x1="928" />
        </branch>
        <branch name="Y2">
            <wire x2="880" y1="336" y2="336" x1="720" />
            <wire x2="880" y1="336" y2="624" x1="880" />
            <wire x2="1264" y1="624" y2="624" x1="880" />
            <wire x2="880" y1="624" y2="1328" x1="880" />
            <wire x2="880" y1="1328" y2="1616" x1="880" />
            <wire x2="1296" y1="1328" y2="1328" x1="880" />
        </branch>
        <branch name="Y1">
            <wire x2="832" y1="384" y2="384" x1="720" />
            <wire x2="1280" y1="384" y2="384" x1="832" />
            <wire x2="832" y1="384" y2="816" x1="832" />
            <wire x2="1280" y1="816" y2="816" x1="832" />
            <wire x2="832" y1="816" y2="1136" x1="832" />
            <wire x2="1296" y1="1136" y2="1136" x1="832" />
            <wire x2="832" y1="1136" y2="1392" x1="832" />
            <wire x2="1296" y1="1392" y2="1392" x1="832" />
            <wire x2="832" y1="1392" y2="1520" x1="832" />
            <wire x2="832" y1="1520" y2="1616" x1="832" />
            <wire x2="1296" y1="1520" y2="1520" x1="832" />
        </branch>
        <branch name="Y0">
            <wire x2="784" y1="432" y2="432" x1="720" />
            <wire x2="784" y1="432" y2="1584" x1="784" />
            <wire x2="784" y1="1584" y2="1616" x1="784" />
            <wire x2="1296" y1="1584" y2="1584" x1="784" />
        </branch>
        <instance x="1280" y="448" name="XLXI_1" orien="R0" />
        <instance x="1264" y="592" name="XLXI_2" orien="R0" />
        <instance x="1264" y="656" name="XLXI_3" orien="R0" />
        <branch name="Y5">
            <wire x2="1024" y1="192" y2="192" x1="720" />
            <wire x2="1024" y1="192" y2="464" x1="1024" />
            <wire x2="1264" y1="464" y2="464" x1="1024" />
            <wire x2="1024" y1="464" y2="944" x1="1024" />
            <wire x2="1296" y1="944" y2="944" x1="1024" />
            <wire x2="1024" y1="944" y2="1616" x1="1024" />
        </branch>
        <instance x="1280" y="880" name="XLXI_4" orien="R0" />
        <instance x="1296" y="1200" name="XLXI_5" orien="R0" />
        <instance x="1296" y="1456" name="XLXI_6" orien="R0" />
        <instance x="1296" y="1648" name="XLXI_7" orien="R0" />
        <iomarker fontsize="28" x="720" y="432" name="Y0" orien="R180" />
        <iomarker fontsize="28" x="720" y="384" name="Y1" orien="R180" />
        <iomarker fontsize="28" x="720" y="336" name="Y2" orien="R180" />
        <iomarker fontsize="28" x="720" y="288" name="Y3" orien="R180" />
        <iomarker fontsize="28" x="720" y="240" name="Y4" orien="R180" />
        <iomarker fontsize="28" x="720" y="192" name="Y5" orien="R180" />
        <iomarker fontsize="28" x="720" y="144" name="Y6" orien="R180" />
        <iomarker fontsize="28" x="720" y="96" name="Y7" orien="R180" />
        <branch name="A">
            <wire x2="1552" y1="352" y2="352" x1="1536" />
            <wire x2="1840" y1="352" y2="352" x1="1552" />
        </branch>
        <iomarker fontsize="28" x="1840" y="352" name="A" orien="R0" />
        <branch name="B">
            <wire x2="1536" y1="496" y2="496" x1="1520" />
            <wire x2="1840" y1="496" y2="496" x1="1536" />
        </branch>
        <branch name="C">
            <wire x2="1504" y1="624" y2="624" x1="1488" />
            <wire x2="1840" y1="624" y2="624" x1="1504" />
        </branch>
        <branch name="D">
            <wire x2="1552" y1="752" y2="752" x1="1536" />
            <wire x2="1840" y1="752" y2="752" x1="1552" />
        </branch>
        <branch name="E">
            <wire x2="1568" y1="1008" y2="1008" x1="1552" />
            <wire x2="1840" y1="1008" y2="1008" x1="1568" />
        </branch>
        <branch name="F">
            <wire x2="1568" y1="1296" y2="1296" x1="1552" />
            <wire x2="1840" y1="1296" y2="1296" x1="1568" />
        </branch>
        <branch name="G">
            <wire x2="1568" y1="1520" y2="1520" x1="1552" />
            <wire x2="1840" y1="1520" y2="1520" x1="1568" />
        </branch>
        <iomarker fontsize="28" x="1840" y="624" name="C" orien="R0" />
        <iomarker fontsize="28" x="1840" y="752" name="D" orien="R0" />
        <iomarker fontsize="28" x="1840" y="1008" name="E" orien="R0" />
        <iomarker fontsize="28" x="1840" y="1296" name="F" orien="R0" />
        <iomarker fontsize="28" x="1840" y="1520" name="G" orien="R0" />
        <iomarker fontsize="28" x="1840" y="496" name="B" orien="R0" />
    </sheet>
</drawing>