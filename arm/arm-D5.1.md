## D5.1 About the ETE protocol

IXCCWQ

An ETE trace unit generates a trace byte stream. The protocol is a byte-based packet protocol, which means that the trace byte stream is constructed of multiple packets, where each packet contains one or more bytes of data.

RBVTNX

Apacket consists of a single header byte, followed by zero or more payload bytes.

## D5.1.1 Encoding schemes

## D5.1.1.1 Field encodings

| I TGRRZ   | Bit Replacement:                                                                                                                                                                                   |
|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| I NKPMZ   | Unsigned LE128n: The data is encoded as an unsigned number. The least significant bits of the number are output in the least significant bits of the packet. Bits not output by the packet are 0 . |
| I WYBBG   | POD: The encoding is specific to the packet.                                                                                                                                                       |
| I QXHHT   | Unary code:                                                                                                                                                                                        |

The sequence for this variable is one of the following:

- A0.
- Anumber of 1s followed by a 0.
- All 1s for the size of the variable, as defined by the packet.

For example, the permitted values for a 4-bit variable are:

- 0b0 .
- 0b10 .
- 0b110 .
- 0b1110 .
- 0b1111 .

## D5.1.1.2 Instruction set encoding

For any virtual instruction address, the instruction set is output as a combination of the following two pieces of information:

- The SF bit encoded in Context packets.
- The sub\_isa encoded by the type of the following groups of packets:
- -Target Address packets.
- -Exception packets.
- -Qpackets.
- -Source Address packets.

The sub\_isa indicates either:

- IS0.
- IS1.

Table D5-1 indicates how the combination of the SF bit and sub\_isa indicate the instruction set.

RFXNDF

| SF Bit   | sub_isa   | Instruction Set   |
|----------|-----------|-------------------|
| 0b0      | IS0       | AArch32 A32       |
| 0b0      | IS1       | AArch32 T32       |
| 0b1      | IS0       | AArch64 A64       |

IWKMNL

The sub\_isa also indicates the alignment of the virtual instruction addresses. Table D5-2 indicates the alignment of each sub\_isa.

## Table D5-2 Virtual instruction address alignment

| sub_isa   | Alignment        |
|-----------|------------------|
| IS0       | Word-aligned     |
| IS1       | Halfword-aligned |

## INSZMB

The following packets encode the sub\_isa:

- Exception Short Address IS0 Packet.
- Exception Short Address IS1 Packet.
- Exception 32-bit Address IS0 Packet.
- Exception 32-bit Address IS1 Packet.
- Exception 64-bit Address IS0 Packet.
- Exception 64-bit Address IS1 Packet.
- Exception 32-bit Address IS0 with Context Packet.
- Exception 32-bit Address IS1 with Context Packet.
- Exception 64-bit Address IS0 with Context Packet.
- Exception 64-bit Address IS1 with Context Packet.
- Target Address Short IS0 Packet.
- Target Address Short IS1 Packet.
- Target Address 32-bit IS0 Packet.
- Target Address 32-bit IS1 Packet.
- Target Address 64-bit IS0 Packet.
- Target Address 64-bit IS1 Packet.
- Target Address with Context 32-bit IS0 Packet.
- Target Address with Context 32-bit IS1 Packet.
- Target Address with Context 64-bit IS0 Packet.
- Target Address with Context 64-bit IS1 Packet.
- Source Address Short IS0 Packet.
- Source Address Short IS1 Packet.
- Source Address 32-bit IS0 Packet.
- Source Address 32-bit IS1 Packet.
- Source Address 64-bit IS0 Packet.
- Source Address 64-bit IS1 Packet.
- Qshort address IS0 Packet.
- Qshort address IS1 Packet.
- Q32-bit address IS0 Packet.
- Q32-bit address IS1 Packet.