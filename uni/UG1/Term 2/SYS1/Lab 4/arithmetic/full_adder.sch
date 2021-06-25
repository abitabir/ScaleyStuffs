<?xml version="1.0" encoding="UTF-8"?>
<drawing version="7">
    <attr value="zynq" name="DeviceFamilyName">
        <trait delete="all:0" />
        <trait editname="all:0" />
        <trait edittrait="all:0" />
    </attr>
    <netlist>
        <signal name="CIN" />
        <signal name="A" />
        <signal name="B" />
        <signal name="COUT" />
        <signal name="XLXN_13" />
        <signal name="SUM" />
        <signal name="XLXN_15" />
        <signal name="XLXN_16" />
        <signal name="XLXN_17" />
        <port polarity="Input" name="CIN" />
        <port polarity="Input" name="A" />
        <port polarity="Input" name="B" />
        <port polarity="Output" name="COUT" />
        <port polarity="Output" name="SUM" />
        <blockdef name="half_adder">
            <timestamp>2020-2-5T11:50:46</timestamp>
            <rect width="256" x="64" y="-128" height="128" />
            <line x2="0" y1="-96" y2="-96" x1="64" />
            <line x2="0" y1="-32" y2="-32" x1="64" />
            <line x2="384" y1="-96" y2="-96" x1="320" />
            <line x2="384" y1="-32" y2="-32" x1="320" />
        </blockdef>
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
        <block symbolname="half_adder" name="XLXI_1">
            <blockpin signalname="A" name="A" />
            <blockpin signalname="B" name="B" />
            <blockpin signalname="XLXN_15" name="SUM" />
            <blockpin signalname="XLXN_17" name="CARRY" />
        </block>
        <block symbolname="half_adder" name="XLXI_2">
            <blockpin signalname="XLXN_15" name="A" />
            <blockpin signalname="CIN" name="B" />
            <blockpin signalname="SUM" name="SUM" />
            <blockpin signalname="XLXN_13" name="CARRY" />
        </block>
        <block symbolname="or2" name="XLXI_3">
            <blockpin signalname="XLXN_13" name="I0" />
            <blockpin signalname="XLXN_17" name="I1" />
            <blockpin signalname="COUT" name="O" />
        </block>
    </netlist>
    <sheet sheetnum="1" width="3520" height="2720">
        <instance x="1040" y="848" name="XLXI_1" orien="R0">
        </instance>
        <instance x="1984" y="880" name="XLXI_3" orien="R0" />
        <branch name="A">
            <wire x2="1024" y1="752" y2="752" x1="1008" />
            <wire x2="1040" y1="752" y2="752" x1="1024" />
        </branch>
        <iomarker fontsize="28" x="1008" y="752" name="A" orien="R180" />
        <branch name="B">
            <wire x2="1024" y1="816" y2="816" x1="1008" />
            <wire x2="1040" y1="816" y2="816" x1="1024" />
        </branch>
        <iomarker fontsize="28" x="1008" y="816" name="B" orien="R180" />
        <iomarker fontsize="28" x="1040" y="944" name="CIN" orien="R180" />
        <branch name="COUT">
            <wire x2="2272" y1="784" y2="784" x1="2240" />
        </branch>
        <iomarker fontsize="28" x="2272" y="784" name="COUT" orien="R0" />
        <iomarker fontsize="28" x="2240" y="944" name="SUM" orien="R0" />
        <branch name="CIN">
            <wire x2="1056" y1="944" y2="944" x1="1040" />
            <wire x2="1056" y1="944" y2="1168" x1="1056" />
            <wire x2="1440" y1="1168" y2="1168" x1="1056" />
        </branch>
        <branch name="XLXN_13">
            <wire x2="1968" y1="1168" y2="1168" x1="1824" />
            <wire x2="1984" y1="816" y2="816" x1="1968" />
            <wire x2="1968" y1="816" y2="1168" x1="1968" />
        </branch>
        <branch name="SUM">
            <wire x2="2224" y1="1104" y2="1104" x1="1824" />
            <wire x2="2240" y1="944" y2="944" x1="2224" />
            <wire x2="2224" y1="944" y2="1104" x1="2224" />
        </branch>
        <branch name="XLXN_15">
            <wire x2="1440" y1="640" y2="640" x1="848" />
            <wire x2="1440" y1="640" y2="752" x1="1440" />
            <wire x2="848" y1="640" y2="1104" x1="848" />
            <wire x2="1424" y1="1104" y2="1104" x1="848" />
            <wire x2="1440" y1="1104" y2="1104" x1="1424" />
            <wire x2="1440" y1="752" y2="752" x1="1424" />
        </branch>
        <instance x="1440" y="1200" name="XLXI_2" orien="R0">
        </instance>
        <branch name="XLXN_17">
            <wire x2="1696" y1="816" y2="816" x1="1424" />
            <wire x2="1696" y1="752" y2="816" x1="1696" />
            <wire x2="1984" y1="752" y2="752" x1="1696" />
        </branch>
    </sheet>
</drawing>