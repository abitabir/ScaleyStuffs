<?xml version="1.0" encoding="UTF-8"?>
<drawing version="7">
    <attr value="zynq" name="DeviceFamilyName">
        <trait delete="all:0" />
        <trait editname="all:0" />
        <trait edittrait="all:0" />
    </attr>
    <netlist>
        <signal name="D0" />
        <signal name="D1" />
        <signal name="D2" />
        <signal name="D3" />
        <signal name="D4" />
        <signal name="D5" />
        <signal name="D6" />
        <signal name="D7" />
        <signal name="Y(6:0)" />
        <signal name="Y(6)" />
        <signal name="Y(5)" />
        <signal name="Y(4)" />
        <signal name="Y(3)" />
        <signal name="Y(2)" />
        <signal name="Y(1)" />
        <signal name="Y(0)" />
        <signal name="A(2:0)" />
        <signal name="A(2)" />
        <signal name="A(1)" />
        <signal name="A(0)" />
        <port polarity="Output" name="Y(6:0)" />
        <port polarity="Input" name="A(2:0)" />
        <blockdef name="onehot_decoder_8">
            <timestamp>2019-10-24T11:54:28</timestamp>
            <rect width="256" x="64" y="-512" height="512" />
            <line x2="0" y1="-256" y2="-256" x1="64" />
            <line x2="384" y1="-480" y2="-480" x1="320" />
            <line x2="384" y1="-416" y2="-416" x1="320" />
            <line x2="384" y1="-352" y2="-352" x1="320" />
            <line x2="384" y1="-288" y2="-288" x1="320" />
            <line x2="384" y1="-224" y2="-224" x1="320" />
            <line x2="384" y1="-160" y2="-160" x1="320" />
            <line x2="384" y1="-96" y2="-96" x1="320" />
            <line x2="384" y1="-32" y2="-32" x1="320" />
            <line x2="0" y1="-192" y2="-192" x1="64" />
            <line x2="0" y1="-320" y2="-320" x1="64" />
        </blockdef>
        <blockdef name="seven_segment_decoder">
            <timestamp>2019-10-24T12:43:25</timestamp>
            <line x2="0" y1="-32" y2="-32" x1="64" />
            <line x2="0" y1="-96" y2="-96" x1="64" />
            <line x2="0" y1="-160" y2="-160" x1="64" />
            <line x2="0" y1="-224" y2="-224" x1="64" />
            <line x2="0" y1="-288" y2="-288" x1="64" />
            <line x2="0" y1="-416" y2="-416" x1="64" />
            <line x2="0" y1="-352" y2="-352" x1="64" />
            <line x2="0" y1="-480" y2="-480" x1="64" />
            <line x2="384" y1="-64" y2="-64" x1="320" />
            <line x2="384" y1="-128" y2="-128" x1="320" />
            <line x2="384" y1="-192" y2="-192" x1="320" />
            <line x2="384" y1="-256" y2="-256" x1="320" />
            <line x2="384" y1="-320" y2="-320" x1="320" />
            <rect width="256" x="64" y="-520" height="520" />
            <line x2="384" y1="-384" y2="-384" x1="320" />
            <line x2="384" y1="-448" y2="-448" x1="320" />
        </blockdef>
        <block symbolname="onehot_decoder_8" name="XLXI_1">
            <blockpin signalname="A(1)" name="B" />
            <blockpin signalname="D0" name="Y0" />
            <blockpin signalname="D1" name="Y1" />
            <blockpin signalname="D2" name="Y2" />
            <blockpin signalname="D3" name="Y3" />
            <blockpin signalname="D4" name="Y4" />
            <blockpin signalname="D5" name="Y5" />
            <blockpin signalname="D6" name="Y6" />
            <blockpin signalname="D7" name="Y7" />
            <blockpin signalname="A(0)" name="A" />
            <blockpin signalname="A(2)" name="C" />
        </block>
        <block symbolname="seven_segment_decoder" name="XLXI_3">
            <blockpin signalname="D7" name="Y7" />
            <blockpin signalname="D6" name="Y6" />
            <blockpin signalname="D4" name="Y4" />
            <blockpin signalname="D3" name="Y3" />
            <blockpin signalname="D2" name="Y2" />
            <blockpin signalname="D1" name="Y1" />
            <blockpin signalname="D0" name="Y0" />
            <blockpin signalname="D5" name="Y5" />
            <blockpin signalname="Y(0)" name="A" />
            <blockpin signalname="Y(1)" name="B" />
            <blockpin signalname="Y(2)" name="C" />
            <blockpin signalname="Y(3)" name="D" />
            <blockpin signalname="Y(4)" name="E" />
            <blockpin signalname="Y(5)" name="F" />
            <blockpin signalname="Y(6)" name="G" />
        </block>
    </netlist>
    <sheet sheetnum="1" width="2720" height="1760">
        <instance x="832" y="1088" name="XLXI_1" orien="R0">
        </instance>
        <branch name="D0">
            <wire x2="1504" y1="608" y2="608" x1="1216" />
        </branch>
        <branch name="D1">
            <wire x2="1504" y1="672" y2="672" x1="1216" />
        </branch>
        <branch name="D2">
            <wire x2="1504" y1="736" y2="736" x1="1216" />
        </branch>
        <branch name="D3">
            <wire x2="1504" y1="800" y2="800" x1="1216" />
        </branch>
        <branch name="D4">
            <wire x2="1504" y1="864" y2="864" x1="1216" />
        </branch>
        <branch name="D5">
            <wire x2="1504" y1="928" y2="928" x1="1216" />
        </branch>
        <branch name="D6">
            <wire x2="1504" y1="992" y2="992" x1="1216" />
        </branch>
        <branch name="D7">
            <wire x2="1504" y1="1056" y2="1056" x1="1216" />
        </branch>
        <instance x="1504" y="1088" name="XLXI_3" orien="R0">
        </instance>
        <branch name="Y(6:0)">
            <wire x2="2320" y1="544" y2="544" x1="2144" />
            <wire x2="2144" y1="544" y2="640" x1="2144" />
            <wire x2="2144" y1="640" y2="704" x1="2144" />
            <wire x2="2144" y1="704" y2="768" x1="2144" />
            <wire x2="2144" y1="768" y2="832" x1="2144" />
            <wire x2="2144" y1="832" y2="896" x1="2144" />
            <wire x2="2144" y1="896" y2="960" x1="2144" />
            <wire x2="2144" y1="960" y2="1024" x1="2144" />
            <wire x2="2144" y1="1024" y2="1056" x1="2144" />
        </branch>
        <bustap x2="2048" y1="640" y2="640" x1="2144" />
        <branch name="Y(6)">
            <wire x2="2048" y1="640" y2="640" x1="1888" />
        </branch>
        <bustap x2="2048" y1="704" y2="704" x1="2144" />
        <bustap x2="2048" y1="768" y2="768" x1="2144" />
        <bustap x2="2048" y1="832" y2="832" x1="2144" />
        <bustap x2="2048" y1="896" y2="896" x1="2144" />
        <bustap x2="2048" y1="960" y2="960" x1="2144" />
        <bustap x2="2048" y1="1024" y2="1024" x1="2144" />
        <branch name="Y(5)">
            <wire x2="2048" y1="704" y2="704" x1="1888" />
        </branch>
        <branch name="Y(4)">
            <wire x2="2048" y1="768" y2="768" x1="1888" />
        </branch>
        <branch name="Y(3)">
            <wire x2="2048" y1="832" y2="832" x1="1888" />
        </branch>
        <branch name="Y(2)">
            <wire x2="2048" y1="896" y2="896" x1="1888" />
        </branch>
        <branch name="Y(1)">
            <wire x2="2048" y1="960" y2="960" x1="1888" />
        </branch>
        <branch name="Y(0)">
            <wire x2="2048" y1="1024" y2="1024" x1="1888" />
        </branch>
        <iomarker fontsize="28" x="2320" y="544" name="Y(6:0)" orien="R0" />
        <branch name="A(2:0)">
            <wire x2="544" y1="544" y2="544" x1="400" />
            <wire x2="544" y1="544" y2="752" x1="544" />
            <wire x2="544" y1="752" y2="768" x1="544" />
            <wire x2="544" y1="768" y2="832" x1="544" />
            <wire x2="544" y1="832" y2="896" x1="544" />
            <wire x2="544" y1="896" y2="912" x1="544" />
        </branch>
        <bustap x2="640" y1="768" y2="768" x1="544" />
        <bustap x2="640" y1="832" y2="832" x1="544" />
        <bustap x2="640" y1="896" y2="896" x1="544" />
        <iomarker fontsize="28" x="400" y="544" name="A(2:0)" orien="R180" />
        <branch name="A(2)">
            <wire x2="832" y1="768" y2="768" x1="640" />
        </branch>
        <branch name="A(1)">
            <wire x2="832" y1="832" y2="832" x1="640" />
        </branch>
        <branch name="A(0)">
            <wire x2="832" y1="896" y2="896" x1="640" />
        </branch>
    </sheet>
</drawing>