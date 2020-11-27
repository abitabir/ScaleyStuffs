<?xml version="1.0" encoding="UTF-8"?>
<drawing version="7">
    <attr value="zynq" name="DeviceFamilyName">
        <trait delete="all:0" />
        <trait editname="all:0" />
        <trait edittrait="all:0" />
    </attr>
    <netlist>
        <signal name="C" />
        <signal name="not_A0" />
        <signal name="not_A1" />
        <signal name="B" />
        <signal name="A" />
        <signal name="XLXN_33" />
        <signal name="Y0" />
        <signal name="Y1" />
        <signal name="Y2" />
        <signal name="Y3" />
        <signal name="Y4" />
        <signal name="Y5" />
        <signal name="Y6" />
        <signal name="Y7" />
        <port polarity="Input" name="C" />
        <port polarity="Input" name="B" />
        <port polarity="Input" name="A" />
        <port polarity="Output" name="Y0" />
        <port polarity="Output" name="Y1" />
        <port polarity="Output" name="Y2" />
        <port polarity="Output" name="Y3" />
        <port polarity="Output" name="Y4" />
        <port polarity="Output" name="Y5" />
        <port polarity="Output" name="Y6" />
        <port polarity="Output" name="Y7" />
        <blockdef name="inv">
            <timestamp>2000-1-1T10:10:10</timestamp>
            <line x2="64" y1="-32" y2="-32" x1="0" />
            <line x2="160" y1="-32" y2="-32" x1="224" />
            <line x2="128" y1="-64" y2="-32" x1="64" />
            <line x2="64" y1="-32" y2="0" x1="128" />
            <line x2="64" y1="0" y2="-64" x1="64" />
            <circle r="16" cx="144" cy="-32" />
        </blockdef>
        <blockdef name="and3">
            <timestamp>2000-1-1T10:10:10</timestamp>
            <line x2="64" y1="-64" y2="-64" x1="0" />
            <line x2="64" y1="-128" y2="-128" x1="0" />
            <line x2="64" y1="-192" y2="-192" x1="0" />
            <line x2="192" y1="-128" y2="-128" x1="256" />
            <line x2="144" y1="-176" y2="-176" x1="64" />
            <line x2="64" y1="-80" y2="-80" x1="144" />
            <arc ex="144" ey="-176" sx="144" sy="-80" r="48" cx="144" cy="-128" />
            <line x2="64" y1="-64" y2="-192" x1="64" />
        </blockdef>
        <block symbolname="inv" name="XLXI_21">
            <blockpin signalname="C" name="I" />
            <blockpin signalname="XLXN_33" name="O" />
        </block>
        <block symbolname="inv" name="XLXI_15">
            <blockpin signalname="B" name="I" />
            <blockpin signalname="not_A0" name="O" />
        </block>
        <block symbolname="inv" name="XLXI_16">
            <blockpin signalname="A" name="I" />
            <blockpin signalname="not_A1" name="O" />
        </block>
        <block symbolname="and3" name="XLXI_22">
            <blockpin signalname="A" name="I0" />
            <blockpin signalname="B" name="I1" />
            <blockpin signalname="C" name="I2" />
            <blockpin signalname="Y7" name="O" />
        </block>
        <block symbolname="and3" name="XLXI_23">
            <blockpin signalname="not_A1" name="I0" />
            <blockpin signalname="B" name="I1" />
            <blockpin signalname="C" name="I2" />
            <blockpin signalname="Y6" name="O" />
        </block>
        <block symbolname="and3" name="XLXI_24">
            <blockpin signalname="A" name="I0" />
            <blockpin signalname="not_A0" name="I1" />
            <blockpin signalname="C" name="I2" />
            <blockpin signalname="Y5" name="O" />
        </block>
        <block symbolname="and3" name="XLXI_25">
            <blockpin signalname="not_A1" name="I0" />
            <blockpin signalname="not_A0" name="I1" />
            <blockpin signalname="C" name="I2" />
            <blockpin signalname="Y4" name="O" />
        </block>
        <block symbolname="and3" name="XLXI_26">
            <blockpin signalname="A" name="I0" />
            <blockpin signalname="B" name="I1" />
            <blockpin signalname="XLXN_33" name="I2" />
            <blockpin signalname="Y3" name="O" />
        </block>
        <block symbolname="and3" name="XLXI_27">
            <blockpin signalname="not_A1" name="I0" />
            <blockpin signalname="B" name="I1" />
            <blockpin signalname="XLXN_33" name="I2" />
            <blockpin signalname="Y2" name="O" />
        </block>
        <block symbolname="and3" name="XLXI_28">
            <blockpin signalname="A" name="I0" />
            <blockpin signalname="not_A0" name="I1" />
            <blockpin signalname="XLXN_33" name="I2" />
            <blockpin signalname="Y1" name="O" />
        </block>
        <block symbolname="and3" name="XLXI_29">
            <blockpin signalname="not_A1" name="I0" />
            <blockpin signalname="not_A0" name="I1" />
            <blockpin signalname="XLXN_33" name="I2" />
            <blockpin signalname="Y0" name="O" />
        </block>
    </netlist>
    <sheet sheetnum="1" width="3520" height="2720">
        <branch name="C">
            <wire x2="720" y1="608" y2="608" x1="576" />
            <wire x2="1024" y1="608" y2="608" x1="720" />
            <wire x2="720" y1="416" y2="608" x1="720" />
            <wire x2="1536" y1="416" y2="416" x1="720" />
            <wire x2="1536" y1="416" y2="752" x1="1536" />
            <wire x2="1744" y1="752" y2="752" x1="1536" />
            <wire x2="1536" y1="752" y2="944" x1="1536" />
            <wire x2="1536" y1="944" y2="952" x1="1536" />
            <wire x2="1536" y1="952" y2="1136" x1="1536" />
            <wire x2="1536" y1="1136" y2="1328" x1="1536" />
            <wire x2="1536" y1="1328" y2="2320" x1="1536" />
            <wire x2="1744" y1="1328" y2="1328" x1="1536" />
            <wire x2="1744" y1="1136" y2="1136" x1="1536" />
            <wire x2="1744" y1="944" y2="944" x1="1536" />
        </branch>
        <branch name="not_A0">
            <wire x2="1344" y1="672" y2="672" x1="1248" />
            <wire x2="1344" y1="672" y2="1200" x1="1344" />
            <wire x2="1344" y1="1200" y2="1392" x1="1344" />
            <wire x2="1344" y1="1392" y2="1968" x1="1344" />
            <wire x2="1344" y1="1968" y2="2160" x1="1344" />
            <wire x2="1344" y1="2160" y2="2320" x1="1344" />
            <wire x2="1744" y1="2160" y2="2160" x1="1344" />
            <wire x2="1744" y1="1968" y2="1968" x1="1344" />
            <wire x2="1744" y1="1392" y2="1392" x1="1344" />
            <wire x2="1744" y1="1200" y2="1200" x1="1344" />
        </branch>
        <branch name="not_A1">
            <wire x2="1296" y1="736" y2="736" x1="1248" />
            <wire x2="1296" y1="736" y2="1072" x1="1296" />
            <wire x2="1296" y1="1072" y2="1456" x1="1296" />
            <wire x2="1296" y1="1456" y2="1840" x1="1296" />
            <wire x2="1296" y1="1840" y2="2224" x1="1296" />
            <wire x2="1296" y1="2224" y2="2320" x1="1296" />
            <wire x2="1744" y1="2224" y2="2224" x1="1296" />
            <wire x2="1744" y1="1840" y2="1840" x1="1296" />
            <wire x2="1744" y1="1456" y2="1456" x1="1296" />
            <wire x2="1744" y1="1072" y2="1072" x1="1296" />
        </branch>
        <branch name="B">
            <wire x2="768" y1="672" y2="672" x1="576" />
            <wire x2="1024" y1="672" y2="672" x1="768" />
            <wire x2="768" y1="480" y2="672" x1="768" />
            <wire x2="1488" y1="480" y2="480" x1="768" />
            <wire x2="1488" y1="480" y2="816" x1="1488" />
            <wire x2="1488" y1="816" y2="1008" x1="1488" />
            <wire x2="1488" y1="1008" y2="1584" x1="1488" />
            <wire x2="1488" y1="1584" y2="1776" x1="1488" />
            <wire x2="1488" y1="1776" y2="2320" x1="1488" />
            <wire x2="1744" y1="1776" y2="1776" x1="1488" />
            <wire x2="1744" y1="1584" y2="1584" x1="1488" />
            <wire x2="1744" y1="1008" y2="1008" x1="1488" />
            <wire x2="1744" y1="816" y2="816" x1="1488" />
        </branch>
        <branch name="Y0">
            <wire x2="2064" y1="2160" y2="2160" x1="2000" />
        </branch>
        <branch name="Y1">
            <wire x2="2064" y1="1968" y2="1968" x1="2000" />
        </branch>
        <branch name="Y2">
            <wire x2="2064" y1="1776" y2="1776" x1="2000" />
        </branch>
        <branch name="Y3">
            <wire x2="2064" y1="1584" y2="1584" x1="2000" />
        </branch>
        <branch name="Y4">
            <wire x2="2064" y1="1392" y2="1392" x1="2000" />
        </branch>
        <branch name="Y5">
            <wire x2="2064" y1="1200" y2="1200" x1="2000" />
        </branch>
        <branch name="Y6">
            <wire x2="2064" y1="1008" y2="1008" x1="2000" />
        </branch>
        <branch name="Y7">
            <wire x2="2064" y1="816" y2="816" x1="2000" />
        </branch>
        <instance x="1024" y="640" name="XLXI_21" orien="R0" />
        <instance x="1024" y="704" name="XLXI_15" orien="R0" />
        <instance x="1024" y="768" name="XLXI_16" orien="R0" />
        <instance x="1744" y="944" name="XLXI_22" orien="R0" />
        <instance x="1744" y="1136" name="XLXI_23" orien="R0" />
        <instance x="1744" y="1328" name="XLXI_24" orien="R0" />
        <instance x="1744" y="1520" name="XLXI_25" orien="R0" />
        <instance x="1744" y="1712" name="XLXI_26" orien="R0" />
        <instance x="1744" y="1904" name="XLXI_27" orien="R0" />
        <instance x="1744" y="2096" name="XLXI_28" orien="R0" />
        <instance x="1744" y="2288" name="XLXI_29" orien="R0" />
        <iomarker fontsize="28" x="576" y="608" name="C" orien="R180" />
        <iomarker fontsize="28" x="576" y="672" name="B" orien="R180" />
        <iomarker fontsize="28" x="576" y="736" name="A" orien="R180" />
        <iomarker fontsize="28" x="2064" y="2160" name="Y0" orien="R0" />
        <iomarker fontsize="28" x="2064" y="1968" name="Y1" orien="R0" />
        <iomarker fontsize="28" x="2064" y="1776" name="Y2" orien="R0" />
        <iomarker fontsize="28" x="2064" y="1584" name="Y3" orien="R0" />
        <iomarker fontsize="28" x="2064" y="1392" name="Y4" orien="R0" />
        <iomarker fontsize="28" x="2064" y="1200" name="Y5" orien="R0" />
        <iomarker fontsize="28" x="2064" y="1008" name="Y6" orien="R0" />
        <iomarker fontsize="28" x="2064" y="816" name="Y7" orien="R0" />
        <text style="fontsize:24;fontname:Arial" x="1584" y="2200">NOT A</text>
        <text style="fontsize:24;fontname:Arial" x="1584" y="2140">NOT B</text>
        <text style="fontsize:24;fontname:Arial" x="1584" y="2076">NOT C</text>
        <text style="fontsize:24;fontname:Arial" x="1584" y="2012">A</text>
        <text style="fontsize:24;fontname:Arial" x="1584" y="1948">NOT B</text>
        <text style="fontsize:24;fontname:Arial" x="1584" y="1884">NOT C</text>
        <branch name="A">
            <wire x2="816" y1="736" y2="736" x1="576" />
            <wire x2="1024" y1="736" y2="736" x1="816" />
            <wire x2="816" y1="544" y2="736" x1="816" />
            <wire x2="1440" y1="544" y2="544" x1="816" />
            <wire x2="1440" y1="544" y2="880" x1="1440" />
            <wire x2="1744" y1="880" y2="880" x1="1440" />
            <wire x2="1440" y1="880" y2="1264" x1="1440" />
            <wire x2="1440" y1="1264" y2="1648" x1="1440" />
            <wire x2="1440" y1="1648" y2="2032" x1="1440" />
            <wire x2="1440" y1="2032" y2="2320" x1="1440" />
            <wire x2="1744" y1="2032" y2="2032" x1="1440" />
            <wire x2="1744" y1="1648" y2="1648" x1="1440" />
            <wire x2="1744" y1="1264" y2="1264" x1="1440" />
        </branch>
        <branch name="XLXN_33">
            <wire x2="1392" y1="608" y2="608" x1="1248" />
            <wire x2="1392" y1="608" y2="944" x1="1392" />
            <wire x2="1392" y1="944" y2="1520" x1="1392" />
            <wire x2="1392" y1="1520" y2="1712" x1="1392" />
            <wire x2="1392" y1="1712" y2="1904" x1="1392" />
            <wire x2="1392" y1="1904" y2="2096" x1="1392" />
            <wire x2="1392" y1="2096" y2="2320" x1="1392" />
            <wire x2="1744" y1="2096" y2="2096" x1="1392" />
            <wire x2="1744" y1="1904" y2="1904" x1="1392" />
            <wire x2="1744" y1="1712" y2="1712" x1="1392" />
            <wire x2="1744" y1="1520" y2="1520" x1="1392" />
        </branch>
    </sheet>
</drawing>