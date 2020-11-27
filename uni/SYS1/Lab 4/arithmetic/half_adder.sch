<?xml version="1.0" encoding="UTF-8"?>
<drawing version="7">
    <attr value="zynq" name="DeviceFamilyName">
        <trait delete="all:0" />
        <trait editname="all:0" />
        <trait edittrait="all:0" />
    </attr>
    <netlist>
        <signal name="XLXN_2" />
        <signal name="XLXN_3" />
        <signal name="A" />
        <signal name="B" />
        <signal name="SUM" />
        <signal name="CARRY" />
        <signal name="XLXN_8" />
        <signal name="XLXN_9" />
        <port polarity="Input" name="A" />
        <port polarity="Input" name="B" />
        <port polarity="Output" name="SUM" />
        <port polarity="Output" name="CARRY" />
        <blockdef name="xor2">
            <timestamp>2000-1-1T10:10:10</timestamp>
            <line x2="64" y1="-64" y2="-64" x1="0" />
            <line x2="60" y1="-128" y2="-128" x1="0" />
            <line x2="208" y1="-96" y2="-96" x1="256" />
            <arc ex="44" ey="-144" sx="48" sy="-48" r="56" cx="16" cy="-96" />
            <arc ex="64" ey="-144" sx="64" sy="-48" r="56" cx="32" cy="-96" />
            <line x2="64" y1="-144" y2="-144" x1="128" />
            <line x2="64" y1="-48" y2="-48" x1="128" />
            <arc ex="128" ey="-144" sx="208" sy="-96" r="88" cx="132" cy="-56" />
            <arc ex="208" ey="-96" sx="128" sy="-48" r="88" cx="132" cy="-136" />
        </blockdef>
        <blockdef name="and2">
            <timestamp>2000-1-1T10:10:10</timestamp>
            <line x2="64" y1="-64" y2="-64" x1="0" />
            <line x2="64" y1="-128" y2="-128" x1="0" />
            <line x2="192" y1="-96" y2="-96" x1="256" />
            <arc ex="144" ey="-144" sx="144" sy="-48" r="48" cx="144" cy="-96" />
            <line x2="64" y1="-48" y2="-48" x1="144" />
            <line x2="144" y1="-144" y2="-144" x1="64" />
            <line x2="64" y1="-48" y2="-144" x1="64" />
        </blockdef>
        <block symbolname="xor2" name="XLXI_1">
            <blockpin signalname="B" name="I0" />
            <blockpin signalname="A" name="I1" />
            <blockpin signalname="SUM" name="O" />
        </block>
        <block symbolname="and2" name="XLXI_2">
            <blockpin signalname="B" name="I0" />
            <blockpin signalname="A" name="I1" />
            <blockpin signalname="CARRY" name="O" />
        </block>
    </netlist>
    <sheet sheetnum="1" width="3520" height="2720">
        <instance x="1536" y="912" name="XLXI_1" orien="R0" />
        <branch name="A">
            <wire x2="1472" y1="784" y2="784" x1="1312" />
            <wire x2="1536" y1="784" y2="784" x1="1472" />
            <wire x2="1536" y1="592" y2="592" x1="1472" />
            <wire x2="1472" y1="592" y2="784" x1="1472" />
        </branch>
        <branch name="B">
            <wire x2="1408" y1="848" y2="848" x1="1312" />
            <wire x2="1536" y1="848" y2="848" x1="1408" />
            <wire x2="1536" y1="656" y2="656" x1="1408" />
            <wire x2="1408" y1="656" y2="848" x1="1408" />
        </branch>
        <branch name="SUM">
            <wire x2="1824" y1="816" y2="816" x1="1792" />
        </branch>
        <iomarker fontsize="28" x="1824" y="816" name="SUM" orien="R0" />
        <branch name="CARRY">
            <wire x2="1808" y1="624" y2="624" x1="1792" />
        </branch>
        <iomarker fontsize="28" x="1312" y="784" name="A" orien="R180" />
        <iomarker fontsize="28" x="1312" y="848" name="B" orien="R180" />
        <instance x="1536" y="720" name="XLXI_2" orien="R0" />
        <iomarker fontsize="28" x="1808" y="624" name="CARRY" orien="R0" />
    </sheet>
</drawing>