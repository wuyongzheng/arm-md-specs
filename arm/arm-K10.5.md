## K10.5 Use of the Embedded Trace and Trace Buffer Extensions

This appendix describes a simple trace decompressor. It contains the following sections:

- Trace analyzer.
- ETE common pseudocode
- ETE programming.
- Trace examples.
- Differences between ETM and ETE.
- Context switching.
- Controlling generation of trace buffer management events.

## K10.5.1 Trace analyzer

## K10.5.1.1 Using Trace Info elements to start trace analysis

After the trace analyzer has located an Alignment Synchronization packet and synchronized with the trace byte stream, it must search for the following elements to begin to analyze the trace byte stream:

1. A Trace Info element .
2. A Context element and a Target Address element .

The trace unit might not generate a Context element and Target Address element immediately after it generates a Trace Info element .

If a Cancel element cancels a Trace Info element then the trace analyzer can still use the information from the discarded Trace Info element , but if the Context element and Target Address element are also discarded, then the trace analyzer must wait for the trace unit to generate a new Context element and Target Address element .

## K10.5.1.2 Encountering Trace Info elements after trace analysis has started

The trace unit might generate Trace Info elements periodically, as a result of trace protocol synchronization requests. This is useful if trace is stored in a circular buffer, because it provides multiple points where trace analysis can start. After a trace analyzer observes the first Trace Info element , it can ignore subsequent Trace Info elements in the same trace session because the static trace programming cannot change and the speculation depth is updated by other element types during the trace session.

## K10.5.1.3 Decompression information

To decompress a trace byte stream, the trace analyzer requires a number of values which differ between implementations. All the information required by the decompressor to analyze the trace byte stream is provided in the TRCIDR0 to TRCIDR13 registers.

Table K10-1 lists the static variables required by the decompressing stages and the fields that provide this information.

## Table K10-1 Static trace unit information

| Variable                        | ID Field          | Stage   |
|---------------------------------|-------------------|---------|
| Commit Mode                     | TRCIDR0.COMMOPT   | 1       |
| Virtual context identifier size | TRCIDR2.VMIDSIZE  | 1       |
| Maximum speculation depth       | TRCIDR8.MAXSPEC   | 1       |
| Transactional Memory support    | TRCIDR0.COMMTRANS | 1&2     |
| WFxInstructions                 | TRCIDR2.WFXMODE   | 3       |

IWDKLF

IFCGKX

IBWQGD

IHTFNG

IRGSRY

## K10.5.2 Stage 1, parsing the byte stream

IZLYTH

The first stage of analyzing the trace is to convert from the bits of the trace byte stream to the elements that are encoded in that trace byte stream.

The ETE architecture enables a trace unit to use techniques that can reduce the trace bandwidth and trace storage requirements. Some of these techniques require the trace analyzer to retain some information between packets so that it can successfully analyze future packets.

## K10.5.2.1 Retained state

RZPQMY

The trace analyzer maintains an independent copy of the address history buffer of the last three Target Address elements .

IHDKHN

The address history buffer in the trace analyzer is required to reconstruct the Target Address elements from the trace byte stream.

RJBGCR

The trace analyzer must maintain the current speculation depth of the parsed trace byte stream.

RHDJJV

The trace analyzer must have the maximum speculation depth supported by the trace unit.

RRZNPD

The trace analyzer maintains a copy of the last Timestamp element value decompressed.

INPCCX

The last Timestamp element value in the trace analyzer is required to reconstruct the full timestamp value for a Timestamp Packet.

RZPNYS

The trace analyzer must maintain a copy of the context:

- Context identifier.

- Virtual context identifier.

- Execution state.

- Exception level

- Security state

RMWFSN

The trace analyzer must maintain a copy of the cycle count threshold.

## K10.5.2.1.1 InstructionParserState()

```
// InstructionParserState // ====================== // State of the instruction parser. type InstructionParserState is ( bits(64) timestamp, // The most recently broadcast timestamp value. // The Address History Buffer. array [0..2] of AddressHistoryBufferEntry address_history_buffer, // Context parameters. bits(32) context_id, // Most recently broadcast Context ID. bits(32) vmid, // Most recently broadcast VMID. bits(2) exception_level, // Most recently broadcast Exception level. SecurityLevel security, // Most recently broadcast Security state. boolean sixty_four_bit, // Most recently broadcast AArch state // (32 or 64?). // Speculation integer current_spec_depth, // The current speculation depth. boolean T, // The current transactional state. // Trace Session static integer cc_threshold, // Cycle count threshold value. // Static state integer max_spec_depth, // The maximum speculation depth. boolean commit_mode, // Commit mode. boolean comm_trans // How transactions traced. )
```

IPXZJK

IVJHHN

## K10.5.2.2 Parsing

The first stage of the decompressor is to convert from the trace byte stream to trace element stream. The trace byte stream can start at the an Alignment Sync packet boundary.

## K10.5.2.2.1 Parse\_Trace()

```
// Parse_Trace() // ============= // Parses a trace bytestream generated by an ETE trace unit. Parse_Trace(bits(S) stream) repeat header = ReadAndConsume(8, stream); case header of when '00000000' Parse_ExtensionPacket(header, stream); when '00000001' Parse_TraceInfoPacket(header, stream); when '0000001x' Parse_TimestampPacket(header, stream); when '00000100' TraceOnPacket(); when '00000110' Parse_ExceptionPacket(header, stream); when '00001010' TransactionStartPacket(); when '00001011' TransactionCommitPacket(); when '0000110x' Parse_CycleCountPackets(header, stream); when '0000111x' Parse_CycleCountPackets(header, stream); when '0001xxxx' Parse_CycleCountPackets(header, stream); when '00101101' Parse_CommitPacket(header, stream); when '0010111x' Parse_CancelPackets(header, stream); when '001100xx' Parse_MispredictPacket(header, stream); when '001101xx' Parse_CancelPackets(header, stream); when '00111xxx' Parse_CancelPackets(header, stream); when '01110000' // Ignore packet when '0111xxxx' Parse_EventTracingPacket(header, stream); when '1000000x' Parse_ContextPacket(header, stream); when '1000001x' Parse_AddressWithContextPacket(header, stream); when '10000101' Parse_AddressWithContextPacket(header, stream); when '10000110' Parse_AddressWithContextPacket(header, stream); when '1001000x' Parse_TargetAddressPacket(header, stream); when '10010010' Parse_TargetAddressPacket(header, stream); when '100101xx' Parse_TargetAddressPacket(header, stream); when '1001100x' Parse_TargetAddressPacket(header, stream); when '1001101x' Parse_TargetAddressPacket(header, stream); when '10011101' Parse_TargetAddressPacket(header, stream); when '10011110' Parse_TargetAddressPacket(header, stream); when '1010xxxx' Parse_QPacket(header, stream); when '101100xx' Parse_SourceAddressPacket(header,stream); when '1011010x' Parse_SourceAddressPacket(header,stream); when '1011011x' Parse_SourceAddressPacket(header,stream); when '1011100x' Parse_SourceAddressPacket(header,stream); when '11xxxxxx' Parse_AtomPackets(header, stream); otherwise ReservedEncoding(); until EndOfStream(stream); return;
```

## K10.5.2.3 Alignment Sync packet

The Alignment Sync packet is a unique sequence of bits that identifies the boundary of another packet. The unique sequence is a header byte, 0b00000000 , followed by a minimum of ten payload bytes of 0b00000000 and one final payload byte of 0b10000000 .

## K10.5.2.3.1 Parse\_ExtensionPacket()

```
// Parse_ExtensionPacket() // ======================= // Parses Alignment Synchronization, Discard and Overflow packets.
```

RRVFVY

```
Parse_ExtensionPacket(bits(8) header, bits(S) stream) extension = ReadAndConsume(8, stream); case extension of when '00000000' // A-sync while extension == '00000000' do extension = ReadAndConsume(8, stream); if extension != '10000000' then ReservedEncoding(); when '00000011' // Discard DiscardPacket(); when '00000101' // Overflow OverflowPacket(); otherwise ReservedEncoding(); return;
```

## K10.5.2.4 Discard

The current speculation depth must be reset to 0.

## K10.5.2.4.1 DiscardPacket()

```
// DiscardPacket() // =============== // Processes a Discard packet. DiscardPacket() Emit(DiscardElement()); if DSTATE.IA.T then Emit(TransactionFailureElement()); DSTATE.IA.current_spec_depth = 0; DSTATE.IA.T = FALSE; return;
```

## K10.5.2.5 Overflow

## K10.5.2.5.1 OverflowPacket()

```
// OverflowPacket() // ================ // Processes an Overflow packet. OverflowPacket() Emit(DiscardElement()); Emit(OverflowElement()); if DSTATE.IA.T then Emit(TransactionFailureElement()); DSTATE.IA.T = FALSE; DSTATE.IA.current_spec_depth = 0; return;
```

IJMXMP

RPKZKZ

RLPYLR

## K10.5.2.6 Trace Info

ATrace Info packet indicates where the compression algorithms used by the trace unit have been set to a known architectural state. As the architectural state of the compression algorithms is known a trace analyzer can start decompression of the trace byte stream at this point.

If the trace unit exposes some trace speculation to the trace analyzer then the trace info packet indicates the trace speculation depth at this point in the trace element stream.

If the trace analyzer starts analysis where the trace speculation depth is nonzero then the analyzer should ignore speculation depth of Commit elements .

ATrace Info Packet sets all entries of the address history buffer to have an address of 0x0 and to sub\_isa of IS0.

The current\_spec\_depth is set to the speculation depth indicated in the trace info element.

## K10.5.2.6.1 Parse\_TraceInfoPacket()

```
// Parse_TraceInfoPacket() // ======================= // Parses a Trace Info packet. Parse_TraceInfoPacket(bits(8) header, bits(S) bits(8) INFO = Zeros(); bits(96) SPEC = Zeros(); bits(96) CYCT = Zeros(); bits(8) PLCTL = ReadAndConsume(8, stream); // Extract the INFO section if present if PLCTL<0> == '1' then INFO = ReadAndConsume(8, stream); // Extract the SPEC section if present if PLCTL<2> == '1' then SPEC = ULEB128(stream); // Extract the CYCT section if present if PLCTL<3> == '1' then CYCT = ULEB128(stream); TraceInfoPacket(PLCTL, INFO, SPEC, CYCT); return;
```

```
stream)
```

## K10.5.2.6.2 TraceInfoPacket()

```
// TraceInfoPacket() // ================= // Processes a Trace Info packet. TraceInfoPacket(bits(8) PLCTL, bits(8) INFO, bits(SN) SPEC, bits(CN) CYCT) DSTATE.IA.timestamp = Zeros(); DSTATE.IA.context_id = Zeros(); DSTATE.IA.vmid = Zeros(); DSTATE.IA.exception_level = EL0; DSTATE.IA.security = SecurityLevel_SECURE; DSTATE.IA.sixty_four_bit = FALSE; AddressHistoryBuffer.Reset(); cc_threshold = if INFO<0> == '1' then UInt(CYCT) else 0; DSTATE.IA.current_spec_depth = UInt(SPEC); Emit(TraceInfoElement(INFO<0> == '1', // cc_enabled
```

IGHTQJ

RPSHDJ

RNQHYR

return;

## K10.5.2.7 Trace On

The Trace On packet indicates that there has been a discontinuity in the instruction trace element stream. It is output whenever a gap occurs, after the gap occurs. This means that a Trace On packet is output:

- When trace generation becomes operative, after the first A-Sync and Trace Info packets but before any packet types that indicate any P0 elements .
- After a trace unit buffer overflow. Again, the Trace On packet is output after the A-Sync and Trace Info packets but before any packet types that indicate any P0 elements .
- After gaps caused by filtering. For example, if filtering is applied to the generation of the trace element stream, so that the trace unit only generates trace for a particular program code sequence, the trace unit might spend much of its time in an inactive state, only generating trace periodically. In this case, a Trace On packet is output after each discontinuity in the trace element stream. The Trace On packet must be output before any packet types that indicate any P0 elements .

## K10.5.2.7.1 TraceOnPacket()

```
On packet.
```

```
// TraceOnPacket() // =============== // Processes a Trace TraceOnPacket() Emit(TraceOnElement()); return;
```

## K10.5.2.8 Speculation

The Commit element must modify the current speculation depth.

## K10.5.2.8.1 Parse\_CommitPacket()

```
// Parse_CommitPacket() // ==================== // Parses a Commit packet. Parse_CommitPacket(bits(8) header, bits(32) COMMIT = ULEB128(stream); CommitPacket(COMMIT); return;
```

```
bits(S) stream)
```

## K10.5.2.8.2 CommitPacket()

```
// CommitPacket() // ============== // Processes a Commit packet. CommitPacket(bits(N) COMMIT) Emit(CommitElement(UInt(COMMIT))); UpdateSpecDepth(-UInt(COMMIT)); return;
```

The Cancel element must modify the current speculation depth.

```
cc_threshold, DSTATE.IA.current_spec_depth, INFO<6> == '1'));
```

## K10.5.2.8.3 Parse\_CancelPackets()

```
// Parse_CancelFormatPackets() // =========================== // Parses all the various Cancel packets. Parse_CancelPackets(bits(8) header, bits(S) stream) case header of when '0010111x' // Cancel Format 1 M = header<0>; bits(32) CANCEL = ULEB128(stream); CancelFormat1Packet(M, CANCEL); when '001101xx' // Cancel Format 2 A2 = header<1:0>; CancelFormat2Packet(A2); when '00111xxx' // Cancel Format 3 A = header<0>; CC = header<2:1>; CancelFormat3Packet(CC, A); return;
```

## K10.5.2.8.4 CancelFormat1Packet()

```
// CancelFormat1Packet() // ===================== // Processes a Cancel packet, format 1. CancelFormat1Packet(bit M, bits(N) CANCEL) count = UInt(CANCEL); Emit(CancelElement(count)); UpdateSpecDepth(-count); if M == '1' then Emit(MispredictElement()); return;
```

## K10.5.2.8.5 CancelFormat2Packet()

```
// CancelFormat2Packet() // ===================== // Processes a Cancel packet, format CancelFormat2Packet(bits(2) A) case A of when '01' HandleAtom(Atom_E); when '10' HandleAtom(Atom_E); HandleAtom(Atom_E); when '11' HandleAtom(Atom_N); count = 1; Emit(CancelElement(count)); UpdateSpecDepth(-count); Emit(MispredictElement()); return;
```

```
2.
```

RRVVFW

## K10.5.2.8.6 CancelFormat3Packet()

```
3.
```

```
// CancelFormat3Packet() // ===================== // Processes a Cancel packet, format CancelFormat3Packet(bits(2) CC, bit A) if A == '1' then HandleAtom(Atom_E); count = UInt(CC) + 2; Emit(CancelElement(count)); UpdateSpecDepth(-count); Emit(MispredictElement()); return;
```

## K10.5.2.9 Mispredict

## K10.5.2.9.1 Parse\_MispredictPacket()

```
// Parse_MispredictPacket() // ======================== // Parses a Mispredict packet. Parse_MispredictPacket(bits(8) header, A = header<1:0>; MispredictPacket(A); return;
```

## K10.5.2.9.2 MispredictPacket()

```
packet.
```

```
// MispredictPacket() // ================== // Processes a Mispredict MispredictPacket(bits(2) A) case A of when '01' HandleAtom(Atom_E); when '10' HandleAtom(Atom_E); HandleAtom(Atom_E); when '11' HandleAtom(Atom_N); otherwise Emit(MispredictElement()); return;
```

## K10.5.2.10 Atom packets

Each Atom element decoded from an Atom packet must increment the current speculation depth of this stage of the decompressor.

## K10.5.2.10.1 Parse\_AtomPacket()

```
// Parse_AtomPackets() // =================== // Parses all the various Atom packets. Parse_AtomPackets(bits(8) header, bits(S) stream) case header of when '1111011x' // Atom Format bit A = header<0>; AtomFormat1Packet(A);
```

```
bits(S) stream)
```

```
1
```

```
when '110110xx' // Atom Format 2 bits(2) A = header<1:0>; AtomFormat2Packet(A); when '11111xxx' // Atom Format 3 bits(3) A = header<2:0>; AtomFormat3Packet(A); when '110111xx' // Atom Format 4 bits(2) A = header<1:0>; AtomFormat4Packet(A); when '11110101' // Atom Format 5.1 AtomFormat5_1Packet(); when '11010101', '11010110', '11010111' // Atom Format 5.2 bits(2) A = header<1:0>; AtomFormat5_2Packet(A); when '11xxxxxx' // Atom Format 6 bit A = header<5>; bits(5) COUNT = header<4:0>; AtomFormat6Packet(A, COUNT);
```

return;

## K10.5.2.10.2 AtomFormat1Packet()

```
// AtomFormat1Packet() // =================== // Processes an Atom packet, AtomFormat1Packet(bit A) if A == '1' then HandleAtom(Atom_E); else HandleAtom(Atom_N); return;
```

```
format 1.
```

## K10.5.2.10.3 AtomFormat2Packet()

```
format 2.
```

```
// AtomFormat2Packet() // =================== // Processes an Atom packet, AtomFormat2Packet(bits(2) A) for I = 0 to 1 if A<I> == '1' then HandleAtom(Atom_E); else HandleAtom(Atom_N); return;
```

## K10.5.2.10.4 AtomFormat3Packet()

```
// AtomFormat3Packet() // =================== // Processes an Atom packet, format 3. AtomFormat3Packet(bits(3) A) for I = 0 to 2 if A<I> == '1' then HandleAtom(Atom_E);
```

```
else HandleAtom(Atom_N); return;
```

## K10.5.2.10.5 AtomFormat4Packet()

```
// AtomFormat4Packet() // =================== // Processes an Atom packet, format 4. AtomFormat4Packet(bits(2) A) case A of when '00' HandleAtom(Atom_N); HandleAtom(Atom_E); HandleAtom(Atom_E); HandleAtom(Atom_E); when '01' HandleAtom(Atom_N); HandleAtom(Atom_N); HandleAtom(Atom_N); HandleAtom(Atom_N); when '10' HandleAtom(Atom_N); HandleAtom(Atom_E); HandleAtom(Atom_N); HandleAtom(Atom_E); when '11' HandleAtom(Atom_E); HandleAtom(Atom_N); HandleAtom(Atom_E); HandleAtom(Atom_N); return;
```

## K10.5.2.10.6 AtomFormat5\_1Packet()

```
// AtomFormat5_1Packet() // ===================== // Processes an Atom packet, AtomFormat5_1Packet() HandleAtom(Atom_N); HandleAtom(Atom_E); HandleAtom(Atom_E); HandleAtom(Atom_E); HandleAtom(Atom_E); return;
```

```
format 5.1.
```

## K10.5.2.10.7 AtomFormat5\_2Packet()

```
format 5.2.
```

```
// AtomFormat5_2Packet() // ===================== // Processes an Atom packet, AtomFormat5_2Packet(bits(2) A) case A of when '01' HandleAtom(Atom_N); HandleAtom(Atom_N); HandleAtom(Atom_N); HandleAtom(Atom_N); HandleAtom(Atom_N);
```

RRZFZW

```
when '10' HandleAtom(Atom_N); HandleAtom(Atom_E); HandleAtom(Atom_N); HandleAtom(Atom_E); HandleAtom(Atom_N); when '11' HandleAtom(Atom_E); HandleAtom(Atom_N); HandleAtom(Atom_E); HandleAtom(Atom_N); HandleAtom(Atom_E);
```

return;

## K10.5.2.10.8 AtomFormat6Packet()

```
// AtomFormat6Packet() // =================== // Processes an Atom packet, format 6. AtomFormat6Packet(bit A, bits(5) COUNT) for I = 0 to UInt(COUNT) + 2 HandleAtom(Atom_E); if A == '1' then HandleAtom(Atom_N); else HandleAtom(Atom_E); return;
```

## K10.5.2.11 Q packets

The Qelement must increment the current speculation depth at this stage of the decompressor.

## K10.5.2.11.1 Parse\_QPacket()

```
// Parse_QPacket() // =============== // Parses a Q packet. Parse_QPacket(bits(8) header, bits(S) stream) AddressHistoryBufferEntry entry = AddressHistoryBuffer.Get(0); bits(32) count; TYPE = header<3:0>; case TYPE of when '0000', '0001', '0010' ExactMatchBytes(header, stream); count = ULEB128(stream); QPacket(TYPE, entry, count); when '0101' ShortAddressBytes(IS0, stream); count = ULEB128(stream); QPacket(TYPE, entry, count); when '0110' ShortAddressBytes(IS1, stream); count = ULEB128(stream); QPacket(TYPE, entry, count); when '1010', '1011' LongAddressBytes(header, stream); count = ULEB128(stream);
```

```
QPacket(TYPE, entry, count); when '1100' count = ULEB128(stream); QPacket(TYPE, UNKNOWN_ADDRESS, count); when '1111' otherwise ReservedEncoding();
```

```
// Parse_SourceAddressPacket() // =========================== // Parses a Source Address packet. Parse_SourceAddressPacket(bits(8) header, bits(S) stream) AddressHistoryBufferEntry entry = AddressHistoryBuffer.Get(0); case header of when '10111000' data1 = ReadAndConsume(8, stream); data2 = ReadAndConsume(8, stream); data3 = ReadAndConsume(48, stream); entry.sub_isa = IS0; entry.address<63:0> = AddressHistoryBuffer.Add(entry); AddressHistoryBuffer.Add(entry); UpdateSpecDepth(1); Emit(SourceAddressElement(entry)); when '10111001' data11 = ReadAndConsume(8, stream); data21 = ReadAndConsume(56, stream); a = entry; entry.sub_isa = IS1; entry.address<63:0> = data21:data11<6:0>:'0'; AddressHistoryBuffer.Add(entry); UpdateSpecDepth(1); Emit(SourceAddressElement(entry)); when '10110110' data12 = ReadAndConsume(8, stream);
```

## QPacket(TYPE, UNKNOWN\_ADDRESS, UNKNOWN\_COUNT); return; K10.5.2.11.2 QPacket() // QPacket() // ========= // Processes a Q packet. QPacket(bits(4) TYPE, AddressHistoryBufferEntry A, bits(CN) COUNT) Emit(QElement(UInt(COUNT))); UpdateSpecDepth(1); // The decoding of the Address field is done by the AddressPacket // but this did not Emit the address element. if (TYPE != '11xx' &amp;&amp; TYPE != '00xx') then Emit(TargetAddressElement(A)); return; K10.5.2.12 Source address packets K10.5.2.12.1 Parse\_SourceAddressPacket() data3:data2&lt;6:0&gt;:data1&lt;6:0&gt;:'00';

```
function,
```

RSRPFR

```
data22 = ReadAndConsume(8, stream); data32 = ReadAndConsume(16, stream); a = entry; entry.sub_isa = IS0; entry.address<31:0> = data32:data22<6:0>:data12<6:0>:'00'; AddressHistoryBuffer.Add(entry); UpdateSpecDepth(1); Emit(SourceAddressElement(entry)); when '10110111' data13 = ReadAndConsume(8, stream); data23 = ReadAndConsume(24, stream); a = entry; entry.sub_isa = IS1; entry.address<31:0> = data23:data13<6:0>:'0'; AddressHistoryBuffer.Add(entry); UpdateSpecDepth(1); Emit(SourceAddressElement(entry)); when '10110100' data14 = ReadAndConsume(8, stream); a = entry; entry.sub_isa = IS0; if data14<7> == '1' then data24 = ReadAndConsume(8, stream); entry.address<16:0> = data24<7:0>:data14<6:0>:'00'; else entry.address<8:0> = data14<6:0>:'00'; AddressHistoryBuffer.Add(entry); UpdateSpecDepth(1); Emit(SourceAddressElement(entry)); when '10011101' data15 = ReadAndConsume(8, stream); a = entry; entry.sub_isa = IS0; if data15<7> == '1' then data25 = ReadAndConsume(8, stream); entry.address<15:0> = data25<7:0>:data15<6:0>:'0'; else entry.address<7:0> = data15<6:0>:'0'; AddressHistoryBuffer.Add(entry); UpdateSpecDepth(1); Emit(SourceAddressElement(entry)); when '101100xx' // Exact match q = UInt(header<1:0>); entry = AddressHistoryBuffer.Get(q); AddressHistoryBuffer.Add(entry); UpdateSpecDepth(1); Emit(SourceAddressElement(entry));
```

return;

## K10.5.2.13 Exceptions

The Exception element must increment the current speculation depth at this stage of the decompressor.

## K10.5.2.13.1 Parse\_ExceptionPacket()

```
// Parse_ExceptionPacket() // ======================= // Parses an exception packet.
```

```
Parse_ExceptionPacket(bits(8) header, bits(S) stream) payload = ReadAndConsume(8, stream); bits(2) E; E<0> = payload<0>; E<1> = payload<6>; bits(5) TYPE = payload<5:1>; bits(8) AH; if E == '01' || E == '10' then // Treat the ADDRESS bytes as an Address packet, including // updating the address registers. AH = ReadAndConsume(8, stream); case AH of when '1001000x', '10010010' // Exact Match. ExactMatchBytes(AH, stream); when '10010101' // Short Address IS0. ShortAddressBytes(IS0, stream); when '10010110' // Short Address IS1. ShortAddressBytes(IS1, stream); when '1001101x', '10011101', '10011110' // Long Address. LongAddressBytes(AH, stream); when '1000001x', '10000101', '10000110' // Long Address with LongAddressBytes(AH, stream); // Context. ContextBytes(stream); when '01110000' // Unknown address UnknownAddressHistoryBuffer(); ExceptionPacket(E, TYPE, AH); else ReservedEncoding(); return;
```

## K10.5.2.13.2 ExceptionPacket()

```
// ExceptionPacket() // ================= // Processes an Exception packet. ExceptionPacket(bits(2) E, bits(5) TYPE, bits(8) AH) AddressHistoryBufferEntry entry = AddressHistoryBuffer.Get(0); case E of when '01' if TYPE == '11000' then Emit(TransactionFailureElement()); else Emit(ExceptionElement(UInt(TYPE), entry.address)); when '10' // The new context and address must now be Emitted. if AH<7:4> == '1000' then // Long Address with Context Emit(ContextElement(DSTATE.IA.context_id, DSTATE.IA.vmid, DSTATE.IA.exception_level, DSTATE.IA.security, DSTATE.IA.sixty_four_bit)); Emit(TargetAddressElement(entry)); if TYPE == '00000' && DSTATE.IA.T then Emit(TransactionFailureElement()); Emit(ExceptionElement(UInt(TYPE), entry.address));
```

```
elsif TYPE == '11000' then Emit(TransactionFailureElement()); else Emit(ExceptionElement(UInt(TYPE), entry.address)); otherwise ReservedEncoding(); UpdateSpecDepth(1); return;
```

## K10.5.2.14 Address and context

## K10.5.2.14.1 Parse\_TargetAddressPacket()

```
// Parse_TargetAddressPacket() // =========================== // Parses a Target Address packet. Parse_TargetAddressPacket(bits(8) header, bits(S) stream) case header of when '1001101x', '10011101', '10011110' // Long Address LongAddressBytes(header, stream); when '10010101' // Short Address IS0 ShortAddressBytes(IS0, stream); when '10010110' // Short Address IS1 ShortAddressBytes(IS1, stream); when '1001000x', '10010010' // Exact match ExactMatchBytes(header, stream); AddressHistoryBufferEntry entry = AddressHistoryBuffer.Get(0); Emit(TargetAddressElement(entry)); return;
```

## K10.5.2.14.2 Parse\_LongAddressBytes()

```
// LongAddressBytes() // ================== // Reads and parses the long address form used in some packets. LongAddressBytes(bits(8) header, bits(S) stream) case header<2:0> of when '010' // 32-bit IS0 data32_is0 = ReadAndConsume(16, stream); A8_2 = data32_is0<6:0>; SBZ(data32_is0<7>); A15_9 = data32_is0<14:8>; SBZ(data32_is0<15>); bits(16) A31_16; A31_16 = POD(16, stream); LongAddressPacket(header, A31_16:A15_9:A8_2); when '011' // 32-bit IS1 data32_is1 = ReadAndConsume(8, stream); A7_1 = data32_is1<6:0>; SBZ(data32_is1<7>); A31_8 = POD(24, stream); LongAddressPacket(header, A31_8:A7_1); when '101' // 64-bit IS0 data64_is0 = ReadAndConsume(16, stream); A8_2 = data64_is0<6:0>; SBZ(data64_is0<7>); A15_9 = data64_is0<14:8>; SBZ(data64_is0<15>);
```

```
A63_16 = POD(48, stream); LongAddressPacket(header, A63_16:A15_9:A8_2); when '110' // 64-bit IS1 data64_is1 = ReadAndConsume(8, stream); A7_1 = data64_is1<6:0>; SBZ(data64_is1<7>); A63_8 = POD(56, stream); LongAddressPacket(header, A63_8:A7_1);
```

return;

## K10.5.2.14.3 LongAddressPacket()

```
// LongAddressPacket() // =================== // Parses the long form address used in some packets. LongAddressPacket(bits(8) header, bits(AN) A) a = AddressHistoryBuffer.Get(0); // Called from a variety of packet types, so only look at bits <2:0> of // the header. case header<2:0> of when '010' // 32-bit address, IS0 assert(AN == 30); a.sub_isa = IS0; // address<63:32> unchanged a.address<31:2> = A<29:0>; a.address<1:0> = '00'; when '011' // 32-bit address, IS1 assert(AN == 31); a.sub_isa = IS1; // address<63:32> unchanged a.address<31:1> = A<30:0>; a.address<0> = '0'; when '101' // 64-bit address, IS0 assert(AN == 62); a.sub_isa = IS0; a.address<63:2> = A<61:0>; a.address<1:0> = '00'; when '110' // 64-bit address, IS1 assert(AN == 63); a.sub_isa = IS1; a.address<63:1> = A<62:0>; a.address<0> = '0'; UpdateAddressHistoryBuffer(a.address, a.sub_isa); return;
```

## K10.5.2.14.4 Parse\_ShortAddressBytes()

```
// ShortAddressBytes() // =================== // Reads and parses the short form address used in some packets. ShortAddressBytes(SubISA sub_isa, bits(S) stream) bits(15) data; if sub_isa == IS0 then data = BitReplacement(stream, AddressHistoryBuffer.Get(0).address<16:2>); else
```

RTKBWR

```
data = BitReplacement(stream, AddressHistoryBuffer.Get(0).address<15:1>); ShortAddressPacket(sub_isa, data); return;
```

## K10.5.2.14.5 ShortAddressPacket()

```
// ShortAddressPacket() // ==================== // Parses the short form address used in some packets. ShortAddressPacket(SubISA sub_isa, bits(AN) A) a = AddressHistoryBuffer.Get(0); assert (AN == 7 || AN == 15); case sub_isa of when IS0 // IS0 a.sub_isa = IS0; // address<63:AN+2> unchanged a.address<AN+1:0> = A:'00'; when IS1 // IS1 a.sub_isa = IS1; // address<63:AN+1> unchanged a.address<AN:0> = A:'0'; UpdateAddressHistoryBuffer(a.address, a.sub_isa); return;
```

## K10.5.2.14.6 Parse\_ExactMatchBytes()

```
// ExactMatchBytes() // ================= // Reads and parses an exact address match used in some ExactMatchBytes(bits(8) header, bits(S) stream) QE = header<1:0>; ExactMatchPacket(QE); return;
```

## K10.5.2.14.7 ExactMatchPacket()

```
// ExactMatchPacket() // ================== // Parses an exact address match. ExactMatchPacket(bits(2) QE) q = UInt(QE); AddressHistoryBufferEntry entry AddressHistoryBuffer.Add(entry); return;
```

```
packets.
```

```
= AddressHistoryBuffer.Get(q);
```

The Context element value is created by combining the value encoded in a Context Packet and the last Context element value.

## K10.5.2.14.8 Parse\_AddressWithContextPacket()

```
// Parse_AddressWithContextPacket() // ================================ // Parses a Target Address with Context packet. Parse_AddressWithContextPacket(bits(8) header, bits(S) stream) LongAddressBytes(header, stream); ContextBytes(stream); AddressHistoryBufferEntry entry = AddressHistoryBuffer.Get(0); Emit(ContextElement(DSTATE.IA.context_id, DSTATE.IA.vmid, DSTATE.IA.exception_level, DSTATE.IA.security, DSTATE.IA.sixty_four_bit)); Emit(TargetAddressElement(entry)); return;
```

## K10.5.2.14.9 Parse\_ContextBytes()

```
// ContextBytes() // ============== // Generates a Context packet from the stream. ContextBytes(bits(S) stream) payload = ReadAndConsume(8, stream); EL = payload<1:0>; SBZ(payload<3:2>); SF = payload<4>; NS = payload<5>; V = payload<6>; C = payload<7>; case C:V of when '00' ContextPacket('1', C, V, NS, SF, EL, DSTATE.IA.vmid, DSTATE.IA.context_id); when '01' bits(32) VMID; VMID = POD(32, stream); ContextPacket('1', C, V, NS, SF, EL, VMID, DSTATE.IA.context_id); when '10' context_id = POD(32, stream); ContextPacket('1', C, V, NS, SF, EL, DSTATE.IA.vmid, context_id); when '11' bits(32) VMID; VMID = POD(32, stream); context_id = POD(32, stream); ContextPacket('1', C, V, NS, SF, EL, VMID, context_id); return; // Parse_ContextPacket() // ===================== // Parses a Context packet. Parse_ContextPacket(bits(8) header, bits(S) stream) P = header<0>; if P == '0' then
```

```
ContextPacket(P, '0', '0', '0', '0', '00', DSTATE.IA.vmid, DSTATE.IA.context_id); else ContextBytes(stream); Emit(ContextElement(DSTATE.IA.context_id, DSTATE.IA.vmid, DSTATE.IA.exception_level, DSTATE.IA.security, DSTATE.IA.sixty_four_bit)); return;
```

## K10.5.2.14.10 ContextPacket()

```
// ContextPacket() // =============== // Processes a Context packet. ContextPacket(bit P, bit C, bit V, bit NS, bit SF, bits(2) EL, bits(32) VMID, bits(32) context_id) if P == '1' then if C == '1' then DSTATE.IA.context_id = context_id; if V == '1' then DSTATE.IA.vmid = VMID; DSTATE.IA.exception_level<1:0> = EL<1:0>; if NS == '1' then DSTATE.IA.security = SecurityLevel_NONSECURE; else DSTATE.IA.security = SecurityLevel_SECURE; DSTATE.IA.sixty_four_bit = (SF == '1'); return;
```

## K10.5.2.15 Transactions

## K10.5.2.15.1 TransactionStartPacket()

```
// Transaction Start Packet() // ========================== // Processes a Transaction Start packet. TransactionStartPacket() Emit(TransactionStartElement()); DSTATE.IA.T = TRUE; if DSTATE.IA.comm_trans then UpdateSpecDepth(1); return;
```

## K10.5.2.15.2 TransactionCommitPacket()

```
// TransactionCommitPacket() // ========================= // Processes a Transacition Commit packet. TransactionCommitPacket() Emit(TransactionCommitElement());
```

RKJNMB

```
DSTATE.IA.T = FALSE; return;
```

## K10.5.2.16 Timestamps

The Timestamp element value is created by combining the value encoded in a Timestamp Packet and the last Timestamp element value.

## K10.5.2.16.1 Parse\_TimestampPacket()

```
BitReplacement(stream, DSTATE.IA.timestamp);
```

```
// Parse_TimestampPacket() // ======================= // Parses a Timestamp packet. Parse_TimestampPacket(bits(8) header, bits(S) stream) bit N; bits(64) TS = bits(20) COUNT = Zeros(); N = header<0>; if N == '1' then COUNT = ULEB128(stream); TimestampPacket(N, TS, COUNT); else TimestampPacket(N, TS, COUNT); return;
```

## K10.5.2.16.2 Parse\_CycleCountPackets()

```
// Parse_CycleCountPackets() // ========================= // Parses all the various Cycle Count packets. Parse_CycleCountPackets(bits(8) header, bits(S) stream) case header of when '0000111x' // Cycle Count format 1 bit U = header<0>; bits(32) COMMIT = Zeros(); bits(20) COUNT = Zeros(); if TRCIDR0.COMMOPT == '0' then COMMIT = ULEB128(stream); if U == '0' then COUNT = ULEB128(stream); CycleCountFormat1Packet(U, COMMIT, COUNT); when '0000110x' // Cycle Count format 2 bits(8) payload = POD(8, stream); bits(4) BBBB = payload<3:0>; if TRCIDR0.COMMOPT == '0' then bit F = header<0>; bits(4) AAAA = payload<7:4>; CycleCountFormat2Packet(F, AAAA, BBBB); else CycleCountFormat2Packet('1', '1111', BBBB); when '0001xxxx' // Cycle Count format 3 bits(2) BB = header<1:0>; if TRCIDR0.COMMOPT == '0' then bits(2) AA = header<3:2>; CycleCountFormat3Packet(AA, BB); else CycleCountFormat3Packet('00', BB); return;
```

## K10.5.2.16.3 TimestampPacket()

```
// TimestampPacket() // ================= // Processes a Timestamp packet. TimestampPacket(bit N, bits(64) TS, bits(CN) COUNT) DSTATE.IA.timestamp = TS; if N == '1' then Emit(TimestampElement(UInt(DSTATE.IA.timestamp), UInt(COUNT))); else Emit(TimestampElement(UInt(DSTATE.IA.timestamp), return;
```

## K10.5.2.16.4 CycleCountFormat1Packet()

```
// CycleCountFormat1Packet() // ========================= // Processes a Cycle Count packet, format 1. CycleCountFormat1Packet(bit U, bits(N) COMMIT, bits(20) COUNT) if UInt(COMMIT) > 0 then Emit(CommitElement(UInt(COMMIT))); UpdateSpecDepth(-UInt(COMMIT)); if U == '1' then Emit(CycleCountElement(integer UNKNOWN)); else Emit(CycleCountElement(UInt(COUNT) + DSTATE.IA.cc_threshold)); return;
```

## K10.5.2.16.5 CycleCountFormat2Packet()

```
// CycleCountFormat2Packet() // ========================= // Processes a Cycle Count packet, format 2. CycleCountFormat2Packet(bit F, bits(4) AAAA, bits(4) BBBB) if F == '1' then commit_count = DSTATE.IA.max_spec_depth + UInt(AAAA) else commit_count = UInt(AAAA) + 1; if commit_count > 0 then Emit(CommitElement(commit_count)); UpdateSpecDepth(-commit_count); Emit(CycleCountElement(DSTATE.IA.cc_threshold + UInt(BBBB))); return;
```

## K10.5.2.16.6 CycleCountFormat3Packet()

```
// CycleCountFormat3Packet() // ========================= // Processes a Cycle Count packet, format 3. CycleCountFormat3Packet(bits(2) AA, bits(2) BB) if !DSTATE.IA.commit_mode then Emit(CommitElement(UInt(AA) + 1)); UpdateSpecDepth(-(UInt(AA) + 1)); Emit(CycleCountElement(DSTATE.IA.cc_threshold return;
```

```
integer UNKNOWN));
```

```
15;
```

```
+ UInt(BB)));
```

## K10.5.2.17 Event tracing

## K10.5.2.17.1 Parse\_EventTracingPacket()

```
Parse_EventTracingPacket(bits(8) header, bits(S) stream)
```

```
// Parse_EventTracingPacket() // ========================== // Parses an Event packet. EventTracingPacket(header<3:0>); return;
```

## K10.5.2.17.2 EventTracingPacket()

```
// EventTracingPacket() // ==================== // Processes an Event packet. EventTracingPacket(bits(4) EVENT) for I = 0 to 3 if EVENT<I> == '1' then Emit(EventElement(I)); return;
```

## K10.5.2.18 Functions

## K10.5.2.18.1 ReadAndConsume()

```
// ReadAndConsume() // ================ // Reads the next N bits from the trace byte stream and returns them, also // updating the trace byte stream pointer. bits(N) ReadAndConsume(integer N, bits(S) stream) if DSTATE.stream_ptr == S then print ("Reached end of trace\n"); assert(FALSE); bits(N) data = stream<DSTATE.stream_ptr + N - 1: DSTATE.stream_ptr>; DSTATE.stream_ptr = DSTATE.stream_ptr + N; return data;
```

## K10.5.2.18.2 HandleAtom()

```
// HandleAtom() // ============= // Emits an atom, and updates the speculation HandleAtom(Atom t) Emit(AtomElement(t)); UpdateSpecDepth(1); return;
```

## K10.5.2.18.3 UpdateSpecDepth()

```
// UpdateSpecDepth() // =================== // Update the speculation depth by a number of elements. UpdateSpecDepth(integer count) DSTATE.IA.current_spec_depth = DSTATE.IA.current_spec_depth + count; if DSTATE.IA.current_spec_depth > DSTATE.IA.max_spec_depth then commit_number = DSTATE.IA.current_spec_depth -DSTATE.IA.max_spec_depth; Emit(CommitElement(commit_number)); DSTATE.IA.current_spec_depth = DSTATE.IA.max_spec_depth;
```

```
depth.
```

return;

## K10.5.2.18.4 UpdateAddressHistoryBuffer()

```
SubISA sub_isa)
```

```
// UpdateAddressHistoryBuffer() // ============================ // Adds the given address and sub_isa to the AHB. UpdateAddressHistoryBuffer(bits(64) address, AddressHistoryBuffer.Add(address, sub_isa); return;
```

## K10.5.2.18.5 UnknownAddressHistoryBuffer()

```
// UnknownAddressHistoryBuffer() // ============================= // Adds an unknown address and sub_isa to the UnknownAddressHistoryBuffer() AddressHistoryBuffer.Add(Zeros(), IS0); return;
```

## K10.5.3 Stage 2, speculation resolution

IKRXLC

IRJDHD

RJKLZY

The resolution stage operates on the Elements in turn. The Elements are buffered until their resolution is determined.

K10.5.3.1

Emit

## K10.5.3.1.1 Emit()

```
// Emit() // ====== Emit(Element e) e.committed = FALSE; case e.kind of when ELEM_TRACE_INFO ProcessTraceInfo(e); // Speculation Support when ELEM_CANCEL ProcessCancel(e); when ELEM_COMMIT ProcessCommit(e); when ELEM_DISCARD ProcessDiscard(e); // Transactional Support when ELEM_TRANS_START ProcessTransactionStart(e); when ELEM_TRANS_COMMIT ProcessTransactionCommit(e); when ELEM_TRANS_FAILURE ProcessTransactionFailure(e); // Others otherwise Stack(e);
```

## K10.5.3.2 Trace Info element

The Trace Info element can be used as a point to start decompression of the trace element stream. When the Trace Info element is generated there might still be some speculative P0 elements . The number of speculative P0 elements is indicated by the current speculation depth member of the Trace Info element .

If the analysis of the trace starts with a Trace Info element with a nonzero current speculation depth the decompressor must ignore the Commit element or Cancel elements for these P0 elements as they will not have been observed by the decompressor.

```
AHB.
```

RWGSCJ

INYYFS

## K10.5.3.2.1 ProcessTraceInfo()

```
// ProcessTraceInfo() // ================== // Processes a Trace Info element, resetting the analyzer to a known ProcessTraceInfo(Element e) if ResolutionQueue.Uninitialized() then ResolutionQueue.Initialize(e.payload.current_spec_depth); if e.payload.in_transaction then TransactionQueue.StartTransaction(); Stack(e); return;
```

## K10.5.3.3 Commit element

The Commit element marks a number of P0 elements as resolved, and if at the head of the queue pass these elements onto the next stage of the decompressor.

## K10.5.3.3.1 ProcessCommit()

```
// ProcessCommit() // =============== // Processes a Commit element, committing the given number of speculative // elements. ProcessCommit(Element e) integer I = 0; repeat if !ResolutionQueue.Aligned() then I = I + 1; ResolutionQueue.Align(); else case ResolutionQueue.Front().kind of when ELEM_EXCEPTION, ELEM_ATOM, ELEM_Q, ELEM_SOURCE_ADDRESS if !ResolutionQueue.Front().committed then I = I + 1; ProcessTransaction(ResolutionQueue.Front()); AnalyzeElement(ResolutionQueue.Front()); ResolutionQueue.PopFront(); when ELEM_TRANS_START if (TRCIDR0.COMMTRANS == '0' && !ResolutionQueue.Front().committed) then I = I + 1; ProcessTransaction(ResolutionQueue.Front()); ResolutionQueue.PopFront(); otherwise ProcessTransaction(ResolutionQueue.Front()); ResolutionQueue.PopFront(); until I == e.payload.count; return;
```

## K10.5.3.4 Cancel element

For example, if a Cancel element indicates that the three most recent P0 elements are canceled, then the trace analyzer must discard:

```
state.
```

RSPBCG

- The Cancel element .
- All elements back to, and including, the third most recent P0 element .
- Any Trace On elements encountered in that section of the element stream.

When discarding P0 elements that have been canceled, a trace analyzer must also discard many other element types that occur in the element stream between the Cancel element and the oldest P0 element that the Cancel element cancels. Table K10-2 shows which elements must be discarded.

## Table K10-2 Cancel Element Operation

| Element             | Behavior on cancelation   |
|---------------------|---------------------------|
| Atom                | Remove                    |
| Commit              | Illegal                   |
| Context             | Remove                    |
| Cycle Count         | Process                   |
| Discard             | Illegal                   |
| Exception           | Remove                    |
| Event               | Keep                      |
| Mispredict          | Remove                    |
| Overflow            | Illegal                   |
| Target Address      | Remove                    |
| Source Address      | Remove                    |
| Timestamp           | Process                   |
| Trace Info          | Keep                      |
| Trace On            | Remove                    |
| Transaction Start   | Remove                    |
| Transaction Failure | Remove                    |

RCBYHC

When a Cancel element occurs, a trace analyzer must not discard Cycle Count elements .

RGZWHY

When a Cancel element occurs, a trace analyzer must not discard ETEEvents .

RZLVXG

When a Cancel element occurs, a trace analyzer must discard Mispredict elements .

## K10.5.3.4.1 ProcessCancel()

```
// ProcessCancel() // =============== // Processes a Cancel element, canceling the given number of // elements. ProcessCancel(Element e) integer I = 0; repeat if !ResolutionQueue.Aligned() then I = I + 1; ResolutionQueue.Align(); else case ResolutionQueue.Back().kind of
```

```
speculative
```

IJTJSW

```
when ELEM_ATOM, ELEM_EXCEPTION, ELEM_Q, ELEM_SOURCE_ADDRESS if !ResolutionQueue.Back().committed then I = I + 1; when ELEM_TRANS_START if (TRCIDR0.COMMTRANS == '0' && !ResolutionQueue.Back().committed) then I = I + 1; TransactionQueue.EndTransaction(); when ELEM_CYCLE_COUNT, ELEM_EVENT, ELEM_TRACE_INFO AnalyzeElement(ResolutionQueue.Back()); when ELEM_TIMESTAMP AnalyzeElement(ResolutionQueue.Back()); ResolutionQueue.PopBack(); until I == e.payload.count; return;
```

## K10.5.3.5 Discard element

ILYPKS

A Discard element indicates that tracing has become inactive while uncommitted P0 elements remain.

RYHRPG

The trace analyzer must cancel all speculative P0 elements .

## K10.5.3.5.1 ProcessDiscard()

```
// ProcessDiscard() // ================ // Processes a Discard element, discarding all speculative ProcessDiscard(Element e) while !ResolutionQueue.Aligned() do ResolutionQueue.Align(); while ResolutionQueue.Length() > 0 do case ResolutionQueue.Back().kind of when ELEM_EVENT, ELEM_TRACE_INFO, ELEM_TIMESTAMP AnalyzeElement(ResolutionQueue.Back()); ResolutionQueue.PopBack(); otherwise ResolutionQueue.PopBack(); TransactionQueue.EndTransaction(); return;
```

## K10.5.3.6 Stack

The Elements processed by this stage of the decompressor must be stored temporarily until the speculation has been resolved.

## K10.5.3.6.1 Stack()

```
// Stack() // ======= // Pushes an element onto the resolution Stack(Element e) ResolutionQueue.Push(e); return;
```

```
queue.
```

```
elements.
```

## K10.5.4 Stage 2, transaction resolution

## K10.5.4.1 Transaction

## K10.5.4.1.1 ProcessTransaction()

```
// ProcessTransaction() // ==================== // Push the element into the transaction queue if we are in a // else analyze it immediately. ProcessTransaction(Element e) if TransactionQueue.InTransaction() then TransactionQueue.Push(e); else AnalyzeElement(e);
```

## K10.5.4.2 Transaction Start element

## K10.5.4.2.1 ProcessTransactionStart()

```
// ProcessTransactionStart() // ========================= // Processes a Transaction Start element, marking we are now in a ProcessTransactionStart(Element e) TransactionQueue.StartTransaction(); Stack(e); return;
```

## K10.5.4.3 Transaction Commit element

## K10.5.4.3.1 ProcessTransactionCommit()

```
// ProcessTransactionCommit() // ========================== // Processes a Transaction Commit element, committing all elements // transaction queue and ending the current transaction. ProcessTransactionCommit(Element e) while TransactionQueue.Length() > 0 do AnalyzeElement(TransactionQueue.Front()); TransactionQueue.FrontPop(); TransactionQueue.EndTransaction();
```

## K10.5.4.4 Transaction Failure element

When a Transaction Failure element occurs, the trace analyzer must process the Cycle Count elements if it is maintaining a cumulative cycle count. Otherwise it must discard the Cycle Count elements that are associated with P0 elements within the transaction.

When a Transaction Failure element occurs, a trace analyzer must not discard the ETEEvents .

## K10.5.4.4.1 ProcessTransactionFailure()

```
// ProcessTransactionFailure() // =========================== // Processes a Transaction Failure element, discarding all elements in // the transaction queue and ending the transaction. ProcessTransactionFailure(Element e) TransactionQueue.EndTransaction(); return;
```

RXZBFV

RKPKFL

```
transaction,
```

```
transaction.
```

```
in the
```

## K10.5.5 Stage 3, analysis

## K10.5.5.1

Analyze element

## K10.5.5.1.1 AnalyzeElement()

```
// AnalyzeElement() // ================ // Analyzes any element. AnalyzeElement(Element e) case e.kind of when ELEM_TARGET_ADDRESS AnalyzeTargetAddress(e); when ELEM_CONTEXT AnalyzeContext(e); when ELEM_MISPREDICT AnalyzeMispredict(e); when ELEM_TRACE_ON AnalyzeTraceOn(e); when ELEM_ATOM AnalyzeAtom(e); when ELEM_EXCEPTION AnalyzeException(e); when ELEM_Q AnalyzeQ(e); when ELEM_CANCEL ERROR("cancel element reached analysis when ELEM_COMMIT ERROR("commit element reached analysis when ELEM_DISCARD AnalyzeDiscard(e); when ELEM_OVERFLOW AnalyzeOverflow(e); when ELEM_EVENT AnalyzeEvent(e); when ELEM_TRACE_INFO AnalyzeTraceInfo(e); when ELEM_TIMESTAMP AnalyzeTimestamp(e); when ELEM_CYCLE_COUNT AnalyzeCycleCount(e); when ELEM_SOURCE_ADDRESS AnalyzeSourceAddress(e); otherwise ERROR("Unrecognised element kind in analysis stage"); return;
```

## K10.5.5.2 Retained state

The trace analyzer must maintain a copy of the context:

- Context identifier.
- Virtual context identifier.
- Execution state.
- Exception level.
- Security state.

## K10.5.5.2.1 ReconstructState()

```
// ReconstructState // ================ // Temporary storage of reconstructor state, can change after resolution. type ReconstructState is ( bits(64) address, // Current address bits(32) context_id, // Current context ID bits(32) vmid, // Current VMID bits(2) exception_level, // Current Exception level SecurityLevel security, // Current Security state boolean sixty_four_bit, // Are we in AArch64? SubISA sub_isa // Current sub_isa )
```

## K10.5.5.3 Operation of the return stack

The trace analyzer maintains an independent copy of the return stack which is used to determine when Target Address elements have been removed and then infer the target of indirect P0 instructions .

RGWFMZ

ISZYZF

```
stage"); stage");
```

ILGKYD

RHYMQH

The trace analyzer return stack only operates after a certain point in the tracing flow, that is after the trace analyzer has decoded the trace packets and after all the elements that indicate speculative execution, except for Mispredict elements , have been removed from the trace element stream.

Whenever a Branch with Link instruction is initially traced with an E Atom element , the link return address and sub\_isa are pushed onto the trace analyzer return stack. This means that the trace unit return stack grows with each new entry, until its maximum depth is reached and the oldest entries start being discarded.

RMGHSB Whenever an indirect P0 instruction is traced with a final E Atom element , and no Target Address element is traced before the next P0 element , the top entry of the trace analyzer return stack is removed and the value of that entry is the target of the indirect P0 instruction .

RXSVZC Atrace analyzer is not required to be aware of the depth of the trace unit return stack, and implements a return stack depth of 15 entries.

IGBVND

RGMTBD

Atrace analyzer return stack push always occurs whenever a Branch with Link instruction is traced with an E Atom element , even if the status of the E Atom element later changes to be an N Atom element as a result of a subsequent Mispredict element .

For example, the following sequence might occur:

1. The PE speculatively executes a Branch with Link instruction that the trace unit traces with an E Atom element . The trace unit pushes the target address of the Branch with Link instruction onto the trace unit return stack.
2. The trace analyzer receives the E Atom element and pushes the target address of the Branch with Link instruction onto the trace analyzer return stack.
3. The PE then cancels the speculative execution. The trace unit generates a Mispredict element .
4. The trace analyzer receives the Mispredict element and changes the status of the E Atom element so that it becomes an N Atom element . The trace analyzer then knows which direction the program flow has taken, and also knows that the target address stored at the top of the trace analyzer return stack is mispredicted.

Note: Whenever the trace unit generates a Mispredict element to correct a Branch with Link instruction to an N Atom element , the mispredicted address remains in the return stack because there is no reason to remove it. There are no adverse consequences of leaving such a mispredicted address in the stack.

If more than one Mispredict element is output corresponding to a particular Atom element , the status of the Atom element alternates between E and N until it settles in its final E or N state. If the final state of the Atom element is E, then when the PE executes an indirect P0 instruction and the trace unit compares the target address with the top entry in its return stack, an address match might occur. An address match can only occur if the final status of the Atom element is E.

IMPGDD The trace analyzer never needs to discard the entries in its copy of the return stack. If the trace unit discards the entries in its return stack then the entries in the trace analyzer return stack remain. As more entries are pushed on to the return stack, the old entries are discarded when they are pushed off the end of the stack.

- IWJLDR The trace analyzer does not need to prevent the return stack from being modified while in a branch broadcasting region.

The fact that the trace unit discards the entries in its return stack when entering the branch broadcasting region ensures that the return stack in the trace unit and the return stack in the trace analyzer remain synchronized.

## K10.5.5.3.1 UpdateReturnStack()

```
// UpdateReturnStack() // =================== // Push the given instruction to the return stack UpdateReturnStack(DecodedInst inst) if inst.is_link then nxt_state = DSTATE.current_analyzer_state; nxt_state.address = nxt_state.address + inst.size; if !nxt_state.sixty_four_bit then nxt_state.address<63:32> = Zeros(); ReturnStack.Push(nxt_state.address, return;
```

```
if necessary. nxt_state.sub_isa);
```

## K10.5.5.4 Atom element

RSKGMZ

An Atom element implies that one or more instructions have been traced, up to and including the next P0 instruction .

IVHHGW

Atrace analyzer must analyze each instruction in the program image from the current address until it observes a P0 instruction . This indicates that the PE has executed each instruction between the current address and the P0 instruction .

## K10.5.5.4.1 AnalyzeAtom()

```
// AnalyzeAtom() // ============= // Analyzes an atom element. AnalyzeAtom(Element e) if e.payload.atom_type == Atom_E then DSTATE.most_recent_branch_was_taken = TRUE; else DSTATE.most_recent_branch_was_taken = FALSE; CheckForReturnStackMatch(); if DSTATE.sync_state == ADDRESS_STATE then DSTATE.sync_state = NOT_SYNC_STATE; if DSTATE.sync_state != FULL_SYNC_STATE then // If we are unsure of context or address then we cannot meaningfully // analyze the atom. return; boolean cur_inst_is_branch = FALSE; // Continue logging instructions until we hit a P0 instruction. while !cur_inst_is_branch do if !ProgramImage.DecodeAvailable() then DSTATE.sync_state = CONTEXT_STATE; if DSTATE.return_stack_clear_pending then ReturnStack.Reset(); return; decoded_inst = ProgramImage.DecodeNextInst(); case decoded_inst.branchtype of when InstType_BRANCH_DIR, InstType_BRANCH_INDIR ProcessBranchInstruction(decoded_inst, DSTATE.most_recent_branch_was_taken); cur_inst_is_branch = TRUE; UpdateReturnStack(decoded_inst); when InstType_WFX, InstType_ISB ProcessBranchInstruction(decoded_inst, DSTATE.most_recent_branch_was_taken); cur_inst_is_branch = TRUE; when InstType_OTHER ReconstructState nxt_state = DSTATE.current_analyzer_state; nxt_state.address = nxt_state.address + decoded_inst.size; if !nxt_state.sixty_four_bit then // mask off the left-most bits nxt_state.address<63:32> = Replicate('0', 32); DSTATE.next_analyzer_state = nxt_state; OutputInstruction(decoded_inst); DSTATE.current_analyzer_state = DSTATE.next_analyzer_state; if DSTATE.return_stack_clear_pending then ReturnStack.Reset(); return;
```

RPJFBL

## K10.5.5.5 Context element

## K10.5.5.5.1 AnalyzeContext()

```
// AnalyzeContext() // ================ // Analyzes a context element. AnalyzeContext(Element e) DSTATE.current_analyzer_state.context_id = e.payload.context_id; DSTATE.current_analyzer_state.vmid = e.payload.vmid; DSTATE.current_analyzer_state.security = e.payload.security; DSTATE.current_analyzer_state.exception_level = e.payload.exception_level; DSTATE.current_analyzer_state.sixty_four_bit = e.payload.sixty_four_bit; case DSTATE.sync_state of when NOT_SYNC_STATE DSTATE.sync_state = CONTEXT_STATE; when ADDRESS_STATE DSTATE.sync_state = FULL_SYNC_STATE; otherwise return;
```

## K10.5.5.6 Exception element

For an Exception element , a trace analyzer must analyze each instruction from the current address, up to but not including the exception return address that the element provides. The PE has executed each instruction in that address range. The number of instructions that are executed can be zero.

Note: Trace analysis tools must be aware, that if PE execution is at the top of memory space, the address that the Exception element provides might be lower than the target address of the most recent P0 element .

## K10.5.5.6.1 AnalyzeException()

```
// AnalyzeException() // ================== // Analyzes an exception element. AnalyzeException(Element e) CheckForReturnStackMatch(); if DSTATE.sync_state == CONTEXT_STATE then DSTATE.sync_state = NOT_SYNC_STATE; if DSTATE.sync_state != FULL_SYNC_STATE then return; integer PER = UInt(e.payload.address); if (ExceptionWithUnknownAddress(e)) then continue_forward = FALSE; elsif UInt(DSTATE.current_analyzer_state.address) < PER then continue_forward = TRUE; else continue_forward = FALSE; // Continue logging instructions until we reach the specified address. while continue_forward do if !ProgramImage.DecodeAvailable() then DSTATE.sync_state = CONTEXT_STATE; if DSTATE.return_stack_clear_pending then ReturnStack.Reset(); return; decoded_inst = ProgramImage.DecodeNextInst(); if decoded_inst.branchtype == InstType_OTHER then ReconstructState nxt_state = DSTATE.current_analyzer_state;
```

RVDRPP

RYJHMV

IGWZMF

```
nxt_state.address = nxt_state.address + decoded_inst.size; DSTATE.next_analyzer_state = nxt_state; if !DSTATE.next_analyzer_state.sixty_four_bit then // mask off the left-most bits DSTATE.next_analyzer_state.address<63:32> = Replicate('0', 32); else ProcessBranchInstruction(decoded_inst, FALSE); UpdateReturnStack(decoded_inst); OutputInstruction(decoded_inst); bits(64) next_addr = DSTATE.current_analyzer_state.address + decoded_inst.size; DSTATE.current_analyzer_state.address = next_addr; if !DSTATE.current_analyzer_state.sixty_four_bit then // mask off the left-most bits DSTATE.current_analyzer_state.address<63:32> = Replicate('0', 32); if UInt(DSTATE.current_analyzer_state.address) >= PER then continue_forward = FALSE; if DSTATE.return_stack_clear_pending then ReturnStack.Reset(); return;
```

## K10.5.5.7 Source address element

A Source Address element indicates that one or more instructions have been traced, up to and including the instruction at the address associated with the element.

A Source Address element indicates that the instruction at the address associated with the element was taken.

Atrace analyzer must analyze each instruction in the program image from the current address until it analyzes the instruction at the address associated with the Source Address element . This indicates that the PE has executed each instruction between the current address and that instruction, and each P0 instruction except the final instruction was not taken.

## K10.5.5.7.1 AnalyzeSourceAddress()

```
// AnalyzeSourceAddress() // ====================== // Analyzes a source address element. AnalyzeSourceAddress(Element e) CheckForReturnStackMatch(); if DSTATE.sync_state == ADDRESS_STATE then DSTATE.sync_state = NOT_SYNC_STATE; if DSTATE.sync_state != FULL_SYNC_STATE then // If we are unsure of context or address then we cannot meaningfully // analyze the source address. return; DSTATE.most_recent_branch_was_taken = FALSE; integer address = UInt(e.payload.address); // Continue logging instructions until we hit the specified address. while (UInt(DSTATE.current_analyzer_state.address) <= address) do if !ProgramImage.DecodeAvailable() then DSTATE.sync_state = CONTEXT_STATE; if DSTATE.return_stack_clear_pending then ReturnStack.Reset(); return; decoded_inst = ProgramImage.DecodeNextInst();
```

```
if decoded_inst.branchtype == InstType_OTHER then ReconstructState nxt_state = DSTATE.current_analyzer_state; nxt_state.address = nxt_state.address + decoded_inst.size; DSTATE.next_analyzer_state = nxt_state; if !DSTATE.next_analyzer_state.sixty_four_bit then DSTATE.next_analyzer_state.address<63:32> = Replicate('0', 32); else if DSTATE.current_analyzer_state.address == e.payload.address then DSTATE.most_recent_branch_was_taken = TRUE; ProcessBranchInstruction(decoded_inst, DSTATE.most_recent_branch_was_taken); cur_inst_is_branch = TRUE; UpdateReturnStack(decoded_inst); OutputInstruction(decoded_inst); DSTATE.current_analyzer_state = DSTATE.next_analyzer_state; if DSTATE.return_stack_clear_pending then ReturnStack.Reset(); return;
```

## K10.5.5.8 Target Address element

## K10.5.5.8.1 AnalyzeTargetAddress()

```
e.payload.address; e.payload.sub_isa;
```

```
// AnalyzeTargetAddress() // ====================== // Analyzes a target address element. AnalyzeTargetAddress(Element e) DSTATE.current_analyzer_state.address = DSTATE.current_analyzer_state.sub_isa = case DSTATE.sync_state of when NOT_SYNC_STATE DSTATE.sync_state = ADDRESS_STATE; when CONTEXT_STATE DSTATE.sync_state = FULL_SYNC_STATE; otherwise return;
```

## K10.5.5.9 Trace Info element

## K10.5.5.9.1 AnalyzeTraceInfo()

```
// AnalyzeTraceInfo() // ================== // Analyzes a trace info element. AnalyzeTraceInfo(Element e) CheckForReturnStackMatch(); return_stack_clear_pending = return;
```

## K10.5.5.10

Trace On element

## K10.5.5.10.1 AnalyzeTraceOn()

```
TRUE;
```

RZRVMZ

IJYPQC

IHPQFK

```
// AnalyzeTraceOn() // ================ // Analyzes a trace on element. AnalyzeTraceOn(Element e) return_stack_clear_pending = TRUE; DSTATE.sync_state = NOT_SYNC_STATE; return;
```

## K10.5.5.11 Mispredict element

When a Mispredict element corresponds to an Atom element for a direct P0 instruction , before the trace analyzer can calculate the target of the direct P0 instruction , it must apply any applicable Mispredict elements so that it can determine whether it is an E Atom element or an N Atom element .

## K10.5.5.11.1 AnalyzeMispredict()

```
// AnalyzeMispredict() // =================== // Analyzes a mispredict element. AnalyzeMispredict(Element e) DSTATE.most_recent_branch_was_taken = !DSTATE.most_recent_branch_was_taken; ReconstructState nxt_state; nxt_state = UpdateBranchState(DSTATE.most_recent_branch_decoded_inst, DSTATE.most_recent_branch_state, DSTATE.most_recent_branch_was_taken); DSTATE.current_analyzer_state = nxt_state; return;
```

## K10.5.5.12 ETEEvent element

## K10.5.5.12.1 AnalyzeEvent()

```
element.
```

```
// AnalyzeEvent() // ============== // Analyzes an event AnalyzeEvent(Element e);
```

## K10.5.5.13 Discard element

When a trace analyzer encounters a Discard element it must be aware that if the last committed P0 element is a conditional P0 instruction , the E or N status of that Atom element might not be correct. This is because the trace unit might be unable to generate any Mispredict elements that the conditional P0 instruction might require.

If the last P0 instruction is an indirect P0 instruction then the target address indicated in the trace stream might be incorrect. This is because the trace unit might be unable to generate any Target Address elements that the indirect P0 instruction might require.

## K10.5.5.13.1 AnalyzeDiscard()

```
= NOT_SYNC_STATE;
```

```
// AnalyzeDiscard() // ================ // Analyzes a discard element. AnalyzeDiscard(Element e) DSTATE.sync_state return;
```

ITXGPZ

## K10.5.5.14 Overflow element

## K10.5.5.14.1 AnalyzeOverflow()

```
= NOT_SYNC_STATE;
```

```
// AnalyzeOverflow() // ================= // Analyzes an overflow element. AnalyzeOverflow(Element e) DSTATE.sync_state return;
```

## K10.5.5.15 Q element

When a trace analyzer encounters a Qelement which has a count of M executed instructions, it must proceed through the program image, analyzing each instruction until it has analyzed M instructions. If it encounters a conditional P0 instruction , the status of the condition code check for that instruction is UNKNOWN. The status of these P0 instructions is not explicitly given in the trace element stream but it might be possible to infer the status of a given P0 instruction that is based on other trace that is generated. After the trace analyzer has analyzed M instructions, the following Target Address element indicates where PE execution continues.

## K10.5.5.15.1 AnalyzeQ()

```
// AnalyzeQ() // ========== // Analyzes a Q element. AnalyzeQ(Element e) CheckForReturnStackMatch(); q_with_count = e.payload.count > 0; if q_with_count then further_analysis_possible = TRUE; else further_analysis_possible = FALSE; DSTATE.sync_state = CONTEXT_STATE; // If we have no count then just wait to resync, it is not safe to guess i = 0; while further_analysis_possible do if ProgramImage.DecodeAvailable() then decoded_inst = ProgramImage.DecodeNextInst(); addr = DSTATE.current_analyzer_state.address + decoded_inst.size; DSTATE.current_analyzer_state.address = addr; else DSTATE.sync_state = CONTEXT_STATE; return; i = i + 1; further_analysis_possible = (i < e.payload.count); OutputInstruction(decoded_inst); return;
```

## K10.5.5.16 Timestamp element

## K10.5.5.16.1 AnalyzeTimestamp()

```
element.
```

```
// AnalyzeTimestamp() // ================== // Analyzes a timestamp AnalyzeTimestamp(Element e);
```

IHTQDP

RTVWLZ

## K10.5.5.17 Cycle Count element

To produce a total cycle count, a trace analyzer can cumulatively add the values from all Cycle Count elements .

Atrace analyzer must not use the cycle count values in Timestamp elements to produce a total cycle count. Such cycle count values are not a Cycle Count element .

## K10.5.5.17.1 AnalyzeCycleCount()

```
element.
```

```
// AnalyzeCycleCount() // =================== // Analyzes a cycle count AnalyzeCycleCount(Element e);
```

## K10.5.5.18 Functions

## K10.5.5.18.1 OutputInstruction()

```
// OutputInstruction() // =================== // Log that an instruction has been executed. OutputInstruction(DecodedInst inst) DSTATE.inst_out_count = DSTATE.inst_out_count return;
```

```
+ 1;
```

## K10.5.5.18.2 CheckReturnStackMatch()

```
// CheckForReturnStackMatch() // ========================== // Check if there is a return stack match, and log the result. CheckForReturnStackMatch() if DSTATE.sync_state == CONTEXT_STATE then if !ReturnStack.IsEmpty() then ReturnStackEntry top = ReturnStack.Pop(); DSTATE.current_analyzer_state.address DSTATE.current_analyzer_state.sub_isa DSTATE.sync_state = FULL_SYNC_STATE;
```

```
= top.address; = top.sub_isa; return;
```

## K10.5.5.18.3 UpdateBranchState()

```
// UpdateBranchState() // =================== // Returns an updated state based on what was executed. ReconstructState UpdateBranchState(DecodedInst inst, ReconstructState in_state, boolean branch_was_taken) out_state = DSTATE.current_analyzer_state; out_state.address = in_state.address; out_state.sixty_four_bit = in_state.sixty_four_bit; out_state.sub_isa = in_state.sub_isa; if branch_was_taken then if inst.branchtype == InstType_BRANCH_INDIR then DSTATE.sync_state = CONTEXT_STATE; else if inst.branchtype == InstType_BRANCH_DIR then out_state.address = out_state.address + inst.addressoffset; else out_state.address = out_state.address + inst.size;
```

```
if !in_state.sixty_four_bit then out_state.address<63:32> = Zeros(); out_state.sub_isa = inst.next_sub_isa; else out_state.address = out_state.address + inst.size; if !out_state.sixty_four_bit then out_state.address<63:32> = Zeros(); return out_state;
```

## K10.5.5.18.4 ProcessBranchInstruction()

```
// ProcessBranchInstruction() // ========================== // Store current state before a branch instruction, as it could change if there // is a misprediction. ProcessBranchInstruction(DecodedInst inst, boolean branch_was_taken) DSTATE.most_recent_branch_state = DSTATE.current_analyzer_state; DSTATE.most_recent_branch_decoded_inst = inst; DSTATE.most_recent_branch_was_taken = branch_was_taken; DSTATE.next_analyzer_state = UpdateBranchState(inst, DSTATE.current_analyzer_state, branch_was_taken); return;
```

## K10.5.5.18.5 DecodedInst()

```
// DecodedInst // =========== // Data extracted from an instruction. type DecodedInst is ( bits(32) instruction, // The instruction itself InstType branchtype, // Type of P0 instruction boolean is_link, // Is it a linking branch? integer size, // Size (32 or 16) SubISA next_sub_isa, // sub_isa of the following instruction to // executed bits(64) addressoffset )
```

## K10.5.6 ETE common pseudocode

## K10.5.6.1 Element ASL

## K10.5.6.1.1 Atom enumeration

```
// Atom // ==== // Atom enum. Atoms are either E (taken) or N (not enumeration Atom { Atom_E, Atom_N };
```

```
taken).
```

```
be
```

## K10.5.6.1.2 AtomElement()

```
// AtomElement() // ============= // Generates an Atom element based on the given atom. Element AtomElement(Atom t) Element a; a.kind = ELEM_ATOM; a.payload.atom_type = t; return a;
```

## K10.5.6.1.3 QElement()

```
// QElement() // ========== // Generates a Q element based on the number // to resolve. Element QElement(integer count) Element a; a.kind = ELEM_Q; a.payload.count = count; return a;
```

```
of elements
```

## K10.5.6.1.4 CancelElement()

```
// CancelElement() // =============== // Generates a Cancel element based on a given number // of elements to cancel. Element CancelElement(integer count) Element a; a.kind = ELEM_CANCEL; a.payload.count = count; return a;
```

## K10.5.6.1.5 CommitElement()

```
// CommitElement() // =============== // Generates a commit element based on the // number of elements to commit. Element CommitElement(integer count) Element a; a.kind = ELEM_COMMIT; a.payload.count = count; return a;
```

## K10.5.6.1.6 ContextElement()

```
// ContextElement() // ================ // Generates a context element based on context ID, VMID, // Exception level, Security state and AArch32/64 state. Element ContextElement(bits(32) context_id, bits(32) vmid, bits(2) exception_level, SecurityLevel secure, boolean sixty_four_bit)
```

```
Element a; a.kind = ELEM_CONTEXT; a.payload.context_id = context_id; a.payload.vmid = vmid; a.payload.exception_level = exception_level; a.payload.security = secure; a.payload.sixty_four_bit = sixty_four_bit; return a;
```

## K10.5.6.1.7 CycleCountElement()

```
// CycleCountElement() // =================== // Generates a Cycle Count element based on a number of Element CycleCountElement(integer count) Element a; a.kind = ELEM_CYCLE_COUNT; a.payload.count = count; return a;
```

## K10.5.6.1.8 DiscardElement()

```
element.
```

```
// DiscardElement() // ================ // Generates a Discard Element DiscardElement() Element a; a.kind = ELEM_DISCARD; return a;
```

## K10.5.6.1.9 ExceptionElement()

```
// ExceptionElement() // ================== // Generates an Exception element based on the address to branch // to and the type of exception. Element ExceptionElement(integer exception_type, bits(64) address) Element a; a.kind = ELEM_EXCEPTION; a.payload.exception_type = exception_type; a.payload.address = address; return a;
```

## K10.5.6.1.10 EventElement()

```
// EventElement() // ============== // Generates an Event element based on the number of the event that fired. Element EventElement(integer idx) Element a; a.kind = ELEM_EVENT; a.payload.event_id = idx; return a;
```

```
cycles.
```

## K10.5.6.1.11 MispredictElement()

```
element.
```

```
// MispredictElement() // =================== // Generates a Mispredict Element MispredictElement() Element a; a.kind = ELEM_MISPREDICT; return a;
```

## K10.5.6.1.12 OverflowElement()

```
element.
```

```
// OverflowElement() // ================= // Generates an Overflow Element OverflowElement() Element a; a.kind = ELEM_OVERFLOW; return a;
```

## K10.5.6.1.13 TimestampElement()

```
// TimestampElement() // ================== // Generates a Timestamp element based on a timestamp value // and a cycle count value. Element TimestampElement(integer timestamp, integer cycles) Element a; a.kind = ELEM_TIMESTAMP; a.payload.timestamp = timestamp; a.payload.cycle_count = cycles; return a;
```

## K10.5.6.1.14 TraceInfoElement()

```
// TraceInfoElement() // ================== // Generates a Trace Info element based on cycle counting parameters, // speculation depth, and transaction status. Element TraceInfoElement(boolean cc_enabled, integer cc_threshold, integer current_spec_depth, boolean in_transaction) Element a; a.kind = ELEM_TRACE_INFO; a.payload.cc_enabled = cc_enabled; a.payload.cc_threshold = cc_threshold; a.payload.current_spec_depth = current_spec_depth; a.payload.in_transaction = in_transaction; return a;
```

## K10.5.6.1.15 TraceOnElement()

```
On element.
```

```
// TraceOnElement() // ================ // Generates a Trace Element TraceOnElement() Element a; a.kind = ELEM_TRACE_ON; return a;
```

## K10.5.6.1.16 TargetAddressElement()

```
// TargetAddressElement() // ====================== // Generates a Target Address element based on a given // address and sub_isa. Element TargetAddressElement(AddressHistoryBufferEntry Element a; a.kind = ELEM_TARGET_ADDRESS; a.payload.address = reg.address; a.payload.sub_isa = reg.sub_isa; return a;
```

```
reg)
```

## K10.5.6.1.17 SourceAddressElement()

```
// SourceAddressElement() // ====================== // Generates a Source Address element based on an instruction's address // and sub_isa. Element SourceAddressElement(AddressHistoryBufferEntry reg) Element a; a.kind = ELEM_SOURCE_ADDRESS; a.payload.address = reg.address; a.payload.sub_isa = reg.sub_isa; return a;
```

## K10.5.6.1.18 TransactionStartElement()

```
// TransactionStartElement() // ========================= Element TransactionStartElement() Element a; a.kind = ELEM_TRANS_START; return a;
```

## K10.5.6.1.19 TransactionCommitElement()

```
// TransactionCommitElement() // ========================== Element TransactionCommitElement() Element a; a.kind = ELEM_TRANS_COMMIT; return a;
```

## K10.5.6.1.20 TransactionFailureElement()

```
// TransactionFailureElement() // =========================== Element TransactionFailureElement() Element a; a.kind = ELEM_TRANS_FAILURE; return a;
```

## K10.5.6.2 Decompressor enumerations

## K10.5.6.2.1 SubISA enumeration

```
// SubISA // ====== // Represents sub instruction set. // IS0 = AArch32 or AArch64, IS1 = AArch32 Thumb enumeration SubISA { IS0, IS1 };
```

## K10.5.6.2.2 SynchronisationState enumeration

```
// States to represent synchronisation of the reconstructor, // transitions as follows: // _______________________________________________ // | Init State| Input | Final State | // |___________|___________________|______________| // | NOT_SYNC | context element | CONTEXT | // | NOT_SYNC | address element | ADDRESS | // | ADDRESS | context element | FULL_SYNC | // | ADDRESS | overflow element | NOT_SYNC | // | ADDRESS | discard element | NOT_SYNC | // | ADDRESS | trace on element | NOT_SYNC | // | ADDRESS | atom element | NOT_SYNC | // | ADDRESS | exception element | NOT_SYNC | // | CONTEXT | address element | FULL_SYNC | // | CONTEXT | overflow element | NOT_SYNC | // | CONTEXT | discard element | NOT_SYNC | // | CONTEXT | trace on element | NOT_SYNC | // | FULL_SYNC | indirect branch | CONTEXT | // | FULL_SYNC | discard element | NOT_SYNC | // | FULL_SYNC | overflow element | NOT_SYNC | // | FULL_SYNC | trace on element | NOT_SYNC | // |___________|___________________|______________| enumeration SynchronisationState { NOT_SYNC_STATE, // Not syncing, need sync CONTEXT_STATE, // Have context, need address ADDRESS_STATE, // Have address, need context FULL_SYNC_STATE // Fully synced };
```

## K10.5.6.2.3 InstType enumeration

```
// InstType // ======== // Instruction type. Cannot use BranchType as this does not cover other P0 // non-branching instructions (WFE/WFI, ISB). // WFX counts as 'Other' if it is not a P0 element (see TRCIDR2.WFXMODE). enumeration InstType { InstType_BRANCH_DIR, // Direct branch InstType_BRANCH_INDIR, // Indirect branch
```

```
state
```

```
InstType_WFX, // WFI/WFE instruction InstType_ISB, // Instruction barrier InstType_OTHER // Non-P0 instructions };
```

## K10.5.6.3 Decompressor functions

## K10.5.6.3.1 EndOfStream()

```
// EndOfStream() // ============= // Returns TRUE iff all the data in the stream have been consumed. boolean EndOfStream(bits(S) stream);
```

## K10.5.6.3.2 ReservedEncoding()

```
// ReservedEncoding() // ================== // The trace byte stream is not compliant to the protocol. The trace // has to stop. ReservedEncoding();
```

## K10.5.6.3.3 ReadAndConsume()

```
// ReadAndConsume() // ================ // Reads the next N bits from the trace byte stream and // updating the trace byte stream pointer. bits(N) ReadAndConsume(integer N, bits(S) stream);
```

## K10.5.6.3.4 LogDecompressor()

```
// Instrumentation functions // ========================= LogDecompressor(Decomp_Level lvl, string details); LogElem(Decomp_Level lvl, Element e, string details); integer GetNextDebugId(); ERROR(string msg); LogReturnStack(); PrintElement(Element e); string ExcepTypeToStr(integer type_val);
```

## K10.5.6.3.5 SBZ()

```
// SBZ() // ===== // Raise an error if the field B is not zero. SBZ(bits(N) B);
```

## K10.5.6.3.6 ResolutionQueue

```
// ResolutionQueue.Initialize() // ============================ // If decompression starts at a Trace Info element that has a nonzero // speculation depth, the trace analyzer must wait until the speculation // of these unseen P0 elements has been resolved. // // Set the number of unseen P0 elements that are outstanding that need to be // resolved. ResolutionQueue.Initialize(integer i); // ResolutionQueue.Uninitialized() // =============================== // Returns TRUE if the resolution queue is uninitialized.
```

```
analyzer
```

```
returns them, also
```

```
boolean ResolutionQueue.Uninitialized(); // ResolutionQueue.Aligned() // ========================= // Returns TRUE if all the unseen P0 elements have been resolved. boolean ResolutionQueue.Aligned(); // ResolutionQueue.Align() // ======================= // Mark the oldest oldest unseen P0 element as resolved. ResolutionQueue.Align(); // ResolutionQueue.Length() // ======================== // Returns the number of elements in the queue. integer ResolutionQueue.Length(); // ResolutionQueue.PopBack() // ========================= // Discards the element at the back (youngest) of the queue. ResolutionQueue.PopBack(); // ResolutionQueue.Back() // ====================== // Returns the element at the back (youngest) of the queue. Element ResolutionQueue.Back(); // ResolutionQueue.PopFront() // ========================== // Removes the element at the front (oldest) from the queue. ResolutionQueue.PopFront(); // ResolutionQueue.Front() // ======================= // Returns the element at the front (oldest) of the queue. Element ResolutionQueue.Front(); // ResolutionQueue.CommitFront() // ============================= // Commits the element at the front of the queue. ResolutionQueue.CommitFront() // ResolutionQueue.Push() // ====================== // Add element e to the back of the queue. ResolutionQueue.Push(Element e); K10.5.6.3.7 TransactionQueue // TransactionQueue.Length() // ========================= // Return the number of entries in the transaction queue. integer TransactionQueue.Length(); queue.
```

```
// TransactionQueue.FrontPop() // =========================== // Remove the first entry in the transaction queue. TransactionQueue.FrontPop(); // TransactionQueue.Front() // ======================== // Return the element at the front of the transaction Element TransactionQueue.Front(); // TransactionQueue.Push()
```

## // ======================= // Add an element to the back of the transaction queue. TransactionQueue.Push(Element e); // TransactionQueue.InTransaction() // ================================ // Are we currently in a transaction? boolean TransactionQueue.InTransaction(); // TransactionQueue.StartTransaction() // =================================== // Enter a transaction. TransactionQueue.StartTransaction(); // TransactionQueue.EndTransaction() // ================================= // Leave a transaction. TransactionQueue.EndTransaction(); K10.5.6.3.8 ReturnStack // ReturnStack.Reset() // =================== // Resets the return stack. ReturnStack.Reset(); // ReturnStack.Push(bits(64) addr, SubISA sub\_isa) // =============================================== // Pushes onto the return stack. ReturnStack.Push(bits(64) addr, SubISA sub\_isa); // ReturnStack.Pop() // ================= // Pops the top of the return stack. ReturnStackEntry ReturnStack.Pop(); // ReturnStack.IsEmpty() // ===================== // Returns TRUE iff the return stack is empty. boolean ReturnStack.IsEmpty(); K10.5.6.3.9 AddressHistoryBufferEntry() // AddressHistoryBufferEntry // ========================= // An entry in the address history buffer. type AddressHistoryBufferEntry is ( bits(64) address, SubISA sub\_isa ) AddressHistoryBufferEntry UNKNOWN\_ADDRESS; K10.5.6.3.10 AddressHistoryBuffer() // AddressHistoryBuffer.Reset() // ============================ // Resets the address history buffer. AddressHistoryBuffer.Reset() for i = 0 to 2 DSTATE.IA.address\_history\_buffer[i].address = Zeros(); DSTATE.IA.address\_history\_buffer[i].sub\_isa = IS0; return;

```
// AddressHistoryBuffer.Add() // ========================== // Adds an address to the address history buffer. AddressHistoryBuffer.Add(AddressHistoryBufferEntry entry) DSTATE.IA.address_history_buffer[2] = DSTATE.IA.address_history_buffer[1]; DSTATE.IA.address_history_buffer[1] = DSTATE.IA.address_history_buffer[0]; DSTATE.IA.address_history_buffer[0] = entry; return; AddressHistoryBuffer.Add(bits(64) address, SubISA sub_isa) AddressHistoryBufferEntry entry; entry.address = address; entry.sub_isa = sub_isa; AddressHistoryBuffer.Add(entry); return; // AddressHistoryBuffer.Get() // ========================== // Returns the given entry from the address history buffer. AddressHistoryBufferEntry AddressHistoryBuffer.Get(integer n) assert n < 3; return DSTATE.IA.address_history_buffer[n]; K10.5.6.3.11 ProgramImage // ProgramImage.DecodeNextInst() // ============================= // Returns the decoded next instruction in the program image. DecodedInst ProgramImage.DecodeNextInst(); // ProgramImageDecodeAvilable() // ============================ // Returns TRUE iff we are currently inside the program image. boolean ProgramImage.DecodeAvailable(); K10.5.6.3.12 ExceptionWithUnknownAddress() // ExceptionWithUnknownAddress() // ============================= // Does this exception type have an unknown // prefered exception return address. boolean ExceptionWithUnknownAddress(Element e) case e.payload.exception_type<4:0> of when '00000', '11001' return TRUE; when '11000' ERROR("Transation Failure Element"); otherwise return FALSE; K10.5.6.4 Data encodings K10.5.6.4.1 POD() format.
```

```
// POD() // ===== // Return data from stream in Plain Old Data Little Endian bits(N) POD(integer N, bits(S) stream) return ReadAndConsume(N, stream);
```

SPWXHJ

SWPVBX

SXCRYM

SVRJNB

## K10.5.6.4.2 ULEB128()

```
the stream.
```

```
// ULEB128() // ========= // Gets N bits of continuable data from bits(N) ULEB128(bits(S) stream) return BitReplacement(stream, Zeros(N));
```

## K10.5.6.4.3 BitReplacement()

```
// BitReplacement() // ================ // Gets N bits of continuable, bit replacement data from the stream. bits(N) BitReplacement(bits(S) stream, bits(N) original) R = original; I = 0; bits(8) BYTE; repeat BYTE = ReadAndConsume(8, stream); R<I+6:I> = BYTE<6:0>; I = I + 7; until BYTE<7> == '0' || I >= N - 8; if BYTE<7> == '1' then BYTE = ReadAndConsume(8, stream); R<I+7:I> = BYTE; end = N MOD 7; if end == 0 then end = 7; if I + 8 > N then SBZ(BYTE<7:end>); return R;
```

## K10.5.7 ETE programming

## K10.5.7.1 Example code sequences

The enabling sequence should be from the trace sink, such as the trace buffer, to the trace unit. This is to ensure the trace sink is ready to capture trace before the trace unit generates any trace.

The disabling sequence should be from the trace unit to the trace sink. This is to ensure that any buffered trace reaches the trace sink while the trace sink is still enabled.

## K10.5.7.1.1 Enabling the trace unit

The following example describes the code sequence to enable the trace unit.

```
;; Program the trace unit registers, except TRCPRGCTLR ISB ;; Synchronize the System Register updates. MOV x0, #0x1 MSR TRCPRGCTLR, x0 ;; Enable the ETE. ;; Wait for TRCSTATR.IDLE==0 poll_idle ISB ;; Synchronize the write to TRCPRGCTLR MRS x1, TRCSTATR TBNZ x1, #1, poll_idle
```

## K10.5.7.1.2 Disabling the trace unit

The following example describes the code sequence to disable the trace unit.

```
STP x0, x1, [sp, #-16]! MRS x0, TRFCR_EL1 ;; Save the current programming of TRFCR_EL1. MOV x1, #0x3
```

SXJRPQ

## SDNGPX

```
BIC x1, x0, x1 MSR TRFCR_EL1, x1 ;; Clear the values of TRFCR_EL1.ExTRE. ;; to put the PE in to a Trace Prohibited region ISB ;; Synchronize the entry to the Trace Prohibited region TSB CSYNC ;; Ensure that all trace has reached the ;; trace buffer and address translations have ;; taken place. MOV x1, #0x0 MSR TRCPRGCTLR, x1 ;; Disable the trace unit ;; Wait for TRCSTATR.IDLE==1 and TRCSTATR.PMSTABLE==1 poll_idle ISB MRS x1, TRCSTATR AND x1, x1, #3 CMP x1, #3 B.NE poll_idle MSR TRFCR_EL1, x0 ;; Restore the programming of TRFCR_EL1. LDP x0, x1, [sp], #16
```

## K10.5.7.1.3 Example save restore routine

## The following example describes the code sequence for saving the trace unit state over a power down.

```
STP x0, x1, [sp, #-16]! ;; Enter a Trace Prohibited region MRS x0, TRFCR_EL1 ;; Save the current programming of TRFCR_EL1. MOV x1, #0x3 BIC x1, x0, x1 MSR TRFCR_EL1, x1 ;; Clear the values of TRFCR_EL1.ExTRE. ISB ;; Synchronizes the entry to the Trace Prohibited region TSB CSYNC ;; Ensure the trace unit is synchronized MOV x1, #1 MSR OSLAR_EL1, x1 ;; Lock the OS lock ;; Wait for TRCSTATR.PMSTABLE==1 poll_pmstable ISB MRS x1, TRCSTATR TST x1, #2 B.EQ poll_pmstable MSR TRFCR_EL1, x0 ;; Restore the programming of TRFCR_EL1. <save the trace unit registers, including TRCPRGCTLR> ;; Wait for TRCSTATR.IDLE==1 poll_idle ISB MRS x1, TRCSTATR TST x1, #1 B.EQ poll_idle LDP x0, x1, [sp], #16
```

The following example describes the code sequence for restoring the trace unit state when power is restored.

```
<restore the trace unit registers, including STP x0, x1, [sp, #-16]! MOV x0, #0 MSR OSLAR_EL1, x0 ;; Clear the OS lock LDP x0, x1, [sp], #16 ISB
```

```
TRCPRGCTLR>
```

IDHQGM

When programming the trace unit, it is important to be aware that the loops that poll TRCSTATR in Figure D4-2 might never complete. Arm recommends that such scenarios are avoided except in rare conditions. However, some system conditions might prevent a trace unit from either leaving the idle state or becoming idle. In particular, a trace unit might never become idle if the trace unit is unable to output all trace due to a system condition.

STTPKR

If multiple reads of TRCSTATR are required, a Context synchronization event is required between each read of TRCSTATR to ensure any change to the trace unit state is observed.

## K10.5.7.2 Minimal programming

IPDMBT

Table K10-3 gives the values for programming the trace unit to enable tracing of a single process at Non-secure EL0. When FEAT\_RME is implemented, this will enable tracing for both Non-secure EL0 and Realm EL0.

## Table K10-3 Minimal programming values

| Register      | Value                                                                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                                                               |
|---------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| TRCCONFIGR    | 0x000018C1                                                                                                                                                                                                                                                                | Enable: • The return stack. • Global timestamping. • Context identifier tracing. • Virtual context identifier tracing.                                                                                                                                                    |
| TRCEVENTCTL0R | 0x00000000                                                                                                                                                                                                                                                                | Disable all event tracing                                                                                                                                                                                                                                                 |
| TRCEVENTCTL1R | 0x00000000                                                                                                                                                                                                                                                                |                                                                                                                                                                                                                                                                           |
| TRCSTALLCTLR  | 0x00000000                                                                                                                                                                                                                                                                | Disable stalling, if implemented                                                                                                                                                                                                                                          |
| TRCSYNCPR     | 0x0000000C                                                                                                                                                                                                                                                                | Enable trace protocol synchronization every 4096 bytes of trace                                                                                                                                                                                                           |
| TRCTRACEIDR   | Nonzero                                                                                                                                                                                                                                                                   | Set a value for the trace ID                                                                                                                                                                                                                                              |
| TRCTSCTLR     | 0x00000000                                                                                                                                                                                                                                                                | Disable the timestamp event The trace unit still generates timestamps due to other reasons such as trace protocol synchronization.                                                                                                                                        |
| TRCVICTLR     | 0x006F0201                                                                                                                                                                                                                                                                | Enable ViewInst to trace everything, with the start/stop logic started Disable: • EL1 in Non-secure state. • EL2 in Non-secure state. • EL1 in Realm state. • EL2 in Realm state. • EL2-EL0 in Secure state. • EL3.                                                       |
| TRCVIIECTLR   | 0x00000000                                                                                                                                                                                                                                                                | No address range filtering for logic started                                                                                                                                                                                                                              |
| TRCVISSCTLR   | 0x00000000                                                                                                                                                                                                                                                                | No start or stop points for ViewInst                                                                                                                                                                                                                                      |
| S SXJLN       | Disabling tracing of Secure state might not be strictly necessary as secure tracing might be disabled by MDCR_EL3.STE, but Arm recommends not enabling trace for un-required Exception levels, to limit the amount of trace.                                              | Disabling tracing of Secure state might not be strictly necessary as secure tracing might be disabled by MDCR_EL3.STE, but Arm recommends not enabling trace for un-required Exception levels, to limit the amount of trace.                                              |
| S QCWTJ       | Disabling tracing of EL1 and EL2 of Non-secure state might not be strictly necessary as non-secure tracing might be disabled by TRFCR_EL2.E2TRE and TRFCR_EL1.E1TRE, but Arm recommends not enabling trace for un-required Exception levels to limit the amount of trace. | Disabling tracing of EL1 and EL2 of Non-secure state might not be strictly necessary as non-secure tracing might be disabled by TRFCR_EL2.E2TRE and TRFCR_EL1.E1TRE, but Arm recommends not enabling trace for un-required Exception levels to limit the amount of trace. |

IVDBGM

IGFWSJ

## K10.5.7.3 Filtering models

Different trace applications require different usage models of a trace unit. For example, one trace application might only require basic program flow trace, whereas another might require tracing of a specific program function.

The ETE architecture provides for each of these usage models. A trace unit can be implemented with a particular set of implementation options, so that a trade-off between functionality and cost can be achieved in meeting the requirements of a trace application. Discovery of the particular set of implementation is achieved by reading TRCIDR0 to TRCIDR13. In a trace unit that includes all implementation options, the simplest way to use the trace unit is to turn on tracing of all aspects of PE operation and let the trace analyzer pick out the required information. However, full trace comes at a high cost in terms of port bandwidth and trace storage. These costs have an impact on the design of a system, so that a higher pin count and larger buffers might be required.

Atrace unit provides on-chip filtering, that facilitates a reduction of the trace bandwidth and therefore provides for a lower system cost. By suspending and enabling trace during a trace that is run to suit the particular requirements of the trace run, the best use of both port bandwidth and trace storage can be made.

The ETE architecture provides the following basic filtering models:

## Continuous tracing

This is where no filtering is applied. The following modes can be used:

- Continuous instruction tracing only, where only the instruction trace stream is output.

## Instruction-based filtering

This is where instruction tracing, and data tracing if it is implemented and enabled, is active only for certain code sequences, such as for a particular process or function.

For all the possible filtering modes, the trace unit can be programmed before a trace run to enable various options, including:

- Context identifier tracing, if implemented, to indicate to a trace analyzer the Context identifier value.
- Virtual context identifier tracing, if implemented, to distinguish between different virtual machines.
- Cycle counting, to enable a trace analyzer to analyze program performance.
- Global timestamping, if implemented, to enable correlation of the two trace streams with other trace sources in the system.
- Branch broadcasting, if implemented, to force all taken P0 instruction targets to be traced with an explicit target address.

Atrace unit is programmed for continuous instruction tracing when no filtering is applied to the instruction trace stream. When a trace unit is programmed for continuous instruction tracing, ViewInst is always active during a trace run. See Filtering trace generation.

## K10.5.7.4 Filtering used the exclude function

The following table describes the programming for excluding a single address range. When FEAT\_RME is implemented, this applies to both Non-secure EL0 and Realm EL0.

| Register      | Value      | Description                                                                                                    |
|---------------|------------|----------------------------------------------------------------------------------------------------------------|
| TRCCONFIGR    | 0x000018C1 | Enable: • the return stack, • global timestamping, • Context identifier, • Virtual context identifier tracing. |
| TRCEVENTCTL0R | 0x00000000 | Disable all event tracing.                                                                                     |
| TRCEVENTCTL1R | 0x00000000 |                                                                                                                |
| TRCSTALLCTLR  | 0x00000000 | Disable stalling, if implemented.                                                                              |
| TRCSYNCPR     | 0x0000000C | Enable trace protocol synchronization every 4096 bytes of trace.                                               |
| TRCTRACEIDR   | Nonzero    | Set a value for the trace ID.                                                                                  |

| Register    | Value         | Description                                                                                                                                                                                                   |
|-------------|---------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| TRCTSCTLR   | 0x00000000    | Disable the timestamp event. The trace unit still generates timestamps due to other reasons such as trace protocol synchronization.                                                                           |
| TRCVICTLR   | 0x006F0201    | Enable ViewInst to trace everything, with the start/stop logic started. Disable: • EL1 in Non-secure state. • EL2 in Non-secure state. • EL1 in Realm state. • EL2 in Realm state. • EL2-EL0 in Secure state. |
| TRCVIIECTLR | 0x00010000    | • EL3. Use ARC0 for the exclude logic.                                                                                                                                                                        |
| TRCVISSCTLR | 0x00000000    | No start or stop points for ViewInst.                                                                                                                                                                         |
| TRCACATR0   | 0x00000000    | The comparator status to match on all instructions at this Virtual address                                                                                                                                    |
| TRCACVR0    | Start Address |                                                                                                                                                                                                               |
| TRCACATR1   | 0x00000000    | The comparator status to match on all instructions at this Virtual address                                                                                                                                    |
| TRCACVR1    | End Address   |                                                                                                                                                                                                               |

## K10.5.7.5 Filtering used the include function

The following table describes the programming for including a single address range. When FEAT\_RME is implemented, this applies to both Non-secure EL0 and Realm EL0.

IPPMSF

| Register      | Value      | Description                                                                                                                         |
|---------------|------------|-------------------------------------------------------------------------------------------------------------------------------------|
| TRCCONFIGR    | 0x000018C1 | Enable: • the return stack, • global timestamping, • Context identifier, • Virtual context identifier tracing.                      |
| TRCEVENTCTL0R | 0x00000000 | Disable all event tracing.                                                                                                          |
| TRCEVENTCTL1R | 0x00000000 |                                                                                                                                     |
| TRCSTALLCTLR  | 0x00000000 | Disable stalling, if implemented.                                                                                                   |
| TRCSYNCPR     | 0x0000000C | Enable trace protocol synchronization every 4096 bytes of trace.                                                                    |
| TRCTRACEIDR   | Nonzero    | Set a value for the trace ID.                                                                                                       |
| TRCTSCTLR     | 0x00000000 | Disable the timestamp event. The trace unit still generates timestamps due to other reasons such as trace protocol synchronization. |

| Register    | Value         | Description                                                                                                                                                                                                   |
|-------------|---------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| TRCVICTLR   | 0x006F0201    | Enable ViewInst to trace everything, with the start/stop logic started. Disable: • EL1 in Non-secure state. • EL2 in Non-secure state. • EL1 in Realm state. • EL2 in Realm state. • EL2-EL0 in Secure state. |
| TRCVIIECTLR | 0x00000001    | Use ARC0 for the include logic.                                                                                                                                                                               |
| TRCVISSCTLR | 0x00000000    | No start or stop points for ViewInst.                                                                                                                                                                         |
| TRCACATR0   | 0x00000000    | The comparator status to match on all instructions at this Virtual address                                                                                                                                    |
| TRCACVR0    | Start Address |                                                                                                                                                                                                               |
| TRCACATR1   | 0x00000000    | The comparator status to match on all instructions at this Virtual address                                                                                                                                    |
| TRCACVR1    | End Address   |                                                                                                                                                                                                               |

## K10.5.7.6 OS save and restore routines

When the PE is context switching of trace unit the following registers need to save and restored. Not all these registers are necessarily implemented for all implementations. Please refer to the register description page for information on if the register is implemented.

- TRCPRGCTLR
- TRCCONFIGR
- TRCAUXCTLR
- TRCEVENTCTL0R
- TRCEVENTCTL1R
- TRCRSR
- TRCSTALLCTLR
- TRCTSCTLR
- TRCSYNCPR
- TRCCCCTLR
- TRCBBCTLR
- TRCTRACEIDR
- TRCQCTLR
- TRCVICTLR
- TRCVIIECTLR

•

TRCVISSCTLR

- TRCVIPCSSCTLR
- TRCSEQEVR&lt;n&gt;
- TRCSEQRSTEVR
- TRCSEQSTR
- TRCEXTINSELR&lt;n&gt;
- TRCCNTRLDVR&lt;n&gt;
- TRCCNTCTLR&lt;n&gt;
- TRCCNTVR&lt;n&gt;
- TRCIMSPEC&lt;n&gt;
- TRCRSCTLR&lt;n&gt;
- TRCSSCCR&lt;n&gt;
- TRCSSCSR&lt;n&gt;

## SBMBXL

SHYDYT

- TRCSSPCICR&lt;n&gt;
- TRCACVR&lt;n&gt;[31:0]
- TRCACVR&lt;n&gt;[63:32]
- TRCACATR&lt;n&gt;[31:0]
- TRCACATR&lt;n&gt;[63:32]
- TRCCIDCVR&lt;n&gt;[31:0]
- TRCCIDCVR&lt;n&gt;[63:32]
- TRCVMIDCVR&lt;n&gt;[31:0]
- TRCVMIDCVR&lt;n&gt;[63:32]
- TRCCIDCCTLR0
- TRCCIDCCTLR1
- TRCVMIDCCTLR0
- TRCVMIDCCTLR1

If the trace unit has not been programmed since the last context switch then there is no requirement to save and restore the registers.

## K10.5.8 Trace examples

## K10.5.8.1 Basic Examples

IXZCWN

The following example shows basic program trace.

## Table K10-6 Example of program trace

|        | Execution     | Trace elements                                                     | Notes                                                                                                                                                                                                                           |
|--------|---------------|--------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0x1000 | B -> 0x2000   | trace_info( . . . ) trace_on() context() address( 0x1000 ) atom(E) | Tracing begins here, therefore the trace unit must generate both: -A Context element . -A Target Address element . The instruction executed is a taken branch, so in addition, the trace unit must generate an E Atom element . |
| 0x2000 | MOV           |                                                                    |                                                                                                                                                                                                                                 |
| 0x2004 | LDR           |                                                                    |                                                                                                                                                                                                                                 |
| 0x2008 | CMP           |                                                                    |                                                                                                                                                                                                                                 |
| 0x200C | BEQ -> 0x3000 | atom(N)                                                            | This branch is not taken, so the trace unit generates anN Atom element . The N Atom element implies the execution of the three previous instructions and the BEQ instruction.                                                   |
| 0x2010 | STR           |                                                                    |                                                                                                                                                                                                                                 |
|        | IRQ           | exception (IRQ, 0x2014 )                                           | An IRQ occurs. The Exception element indicates the STR instruction was executed.                                                                                                                                                |

IHKPNY

The following example shows basic program trace when filtering is applied. In this example, the trace unit is programmed to exclude all instructions in the address range 0x2000 to 0x200F inclusive, and the trace unit is programmed to start tracing when the instruction at 0x1000 is accessed.

Table K10-7 Example of program trace with filtering

|        | Execution     | Trace   | elements Notes                                                                                                                                                                                                                                                                                       |
|--------|---------------|---------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0x1000 | B -> 0x2000   | Y       | trace_info( . . . ) trace_on() context() address( 0x1000 ) atom(E) Tracing begins here, therefore the trace unit must generate both: -A Context element . - An Target Address element . The instruction executed is a taken branch, so in addition, the trace unit must generate an E Atom element . |
| 0x2000 | MOV           | N       |                                                                                                                                                                                                                                                                                                      |
| 0x2004 | LDR           | N       |                                                                                                                                                                                                                                                                                                      |
| 0x2008 | CMP           | N       |                                                                                                                                                                                                                                                                                                      |
| 0x200C | BEQ -> 0x3000 | N       |                                                                                                                                                                                                                                                                                                      |
| 0x2010 | STR           | Y       | trace_on()                                                                                                                                                                                                                                                                                           |
|        | IRQ           |         | exception (IRQ, 0x2014 ) An IRQ occurs. The Exception element indicates the STR instruction                                                                                                                                                                                                          |

IBXYHM

The example in Table K10-8 shows basic program trace and demonstrates the canceling of some speculative execution because of an exception. In this example the trace unit is programmed to start tracing when the instruction at 0x1000 is accessed.

## Table K10-8 Example of basic program trace when an exception occurs, example one

|        | Execution                           | Trace elements                                              | Notes                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|--------|-------------------------------------|-------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0x1000 | B -> 0x2000                         | trace_info() trace_on() context() address( 0x1000 ) atom(E) | Tracing begins here, therefore the trace unit must generate both: - Context element . - Target Address element The instruction executed is a taken branch, so in addition, the trace unit must generate an E Atom element .                                                                                                                                                                                                                           |
| 0x2000 | MOV                                 |                                                             | None of these instructions are traced as P0 elements , therefore no trace elements are generated.                                                                                                                                                                                                                                                                                                                                                     |
| 0x2004 | LDR                                 |                                                             |                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| 0x2008 | CMP                                 |                                                             |                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| 0x200C | BEQ -> 0x3000 (not taken)           | atom(N)                                                     | This branch is not taken, so the trace unit generates anN Atom element . TheN Atom element implies the execution of the three previous instructions and the BEQ instruction.                                                                                                                                                                                                                                                                          |
| 0x2010 | STR                                 |                                                             | This instruction is not traced as a P0 element , therefore no trace element is generated.                                                                                                                                                                                                                                                                                                                                                             |
|        | Cancel back to and including 0x2000 | cancel(1)                                                   | This cancels theN Atom element that was generated for the branch at 0x200C . The trace analyzer must discard theN Atom element , plus the three instructions that it implied. Note Although PE execution has also canceled execution of the STR instruction, the trace analyzer is unaware of this, because the STR instruction was never traced. This is because no P0 elements were generated that would indicate execution of the STR instruction. |

| Execution            | Trace elements          | Notes                                                                                                                                                            |
|----------------------|-------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| IRQ                  | exception(IRQ, 0x2000 ) | The trace unit generates an Exception element with the address 0x2000 , which indicates no instructions have executed since the target of the branch at 0x1000 . |
| commit all execution | commit(2)               | This commits the E Atom element that was generated for the Branch instruction at 0x1000 , plus the Exception element that was generated for the IRQ exception.   |

IXJLJN

The example in Table K10-9 shows basic program trace, and shows the trace generated when a synchronous Data Abort occurs. In this example the trace unit is programmed to start tracing when the instruction at 0x1000 is accessed.

## Table K10-9 Example of basic program trace when an exception occurs, example two

|        | Execution                                     | Trace elements                                              | Notes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|--------|-----------------------------------------------|-------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0x1000 | B -> 0x2000                                   | trace_info() trace_on() context() address( 0x1000 ) atom(E) | Tracing begins here, therefore the trace unit must generate both: - Context element . - Target Address element . The instruction executed is a taken branch, so in addition, the trace unit must generate an E Atom element .                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| 0x2000 | MOV                                           |                                                             | None of these instructions are traced as P0 elements , therefore no trace elements are generated.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| 0x2004 | LDR                                           |                                                             |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| 0x2008 | CMP                                           |                                                             |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| 0x200C | BEQ -> 0x3000 (not taken)                     | atom(N)                                                     | This branch is not taken, so the trace unit generates anN Atom element . TheN Atom element implies the execution of the three previous instructions and theBEQ instruction.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 0x2010 | STR                                           |                                                             | This instruction is not traced as a P0 element , therefore no trace element is generated.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|        | LDRaborts Cancel back to and including 0x2004 | cancel(1) exception_(data fault, 0x2004 )                   | This cancels theN Atom element that was generated for the branch at 0x200C . The trace analyzer must discard theN Atom element , plus the four instructions that it implied. Note Although PE execution has also canceled execution of the STR instruction, the trace analyzer is unaware of this, because the STR instruction was never traced. This is because no P0 elements were generated that would indicate execution of the STR instruction. The data fault exception occurred at 0x2004 . The Exception element indicates the MOV instruction at 0x2000 was executed. In summary: 1. The MOV instruction was first implied by theN Atom element at 0x200C . However, the trace analyzer canceled this because of the Cancel element . |

|         | Execution                                                                                                                                                                                                                                                                         | Trace elements                                                                                                                                                                                                                                                                    | Notes                                                                                                                                                                                                                                                                             |
|---------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|         | commit all execution                                                                                                                                                                                                                                                              | commit(2)                                                                                                                                                                                                                                                                         | This commits the E Atom element that was generated for the Branch instruction at 0x1000 , plus the Exception element that was generated for the IRQ exception.                                                                                                                    |
| I DLXSS | The example in Table K10-10 extends the example shown in Table K10-9, and shows how exceptions are traced when two exceptions occur without any execution between them. In this example the trace unit is programmed to start tracing when the instruction at 0x1000 is accessed. | The example in Table K10-10 extends the example shown in Table K10-9, and shows how exceptions are traced when two exceptions occur without any execution between them. In this example the trace unit is programmed to start tracing when the instruction at 0x1000 is accessed. | The example in Table K10-10 extends the example shown in Table K10-9, and shows how exceptions are traced when two exceptions occur without any execution between them. In this example the trace unit is programmed to start tracing when the instruction at 0x1000 is accessed. |

## Table K10-10 Example of basic program trace when two consecutive exceptions occur

|        | Execution                                     | Trace elements                                              | Notes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|--------|-----------------------------------------------|-------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0x1000 | B -> 0x2000                                   | trace_info() trace_on() context() address( 0x1000 ) atom(E) | Tracing begins here, therefore the trace unit must generate both: - Context element . - Target Address element . The instruction executed is a taken branch, so in addition, the trace unit must generate an E Atom element .                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| 0x2000 | MOV                                           |                                                             | None of these instructions are traced as P0 elements, therefore no trace elements are generated.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| 0x2004 | LDR                                           |                                                             |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| 0x2008 | CMP                                           |                                                             |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| 0x200C | BEQ -> 0x3000 (not taken)                     | atom(N)                                                     | This branch is not taken, so the trace unit generates anN Atom element . TheN Atom element implies the execution of the three previous instructions and theBEQ instruction.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| 0x2010 | STR                                           |                                                             | This instruction is not traced as a P0 element , therefore no trace element is generated.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|        | LDRaborts Cancel back to and including 0x2004 | cancel(1) exception_(data fault, 0x2004 )                   | This cancels theN Atom element that was generated for the branch at 0x200C . The trace analyzer must discard the N Atom element , plus the four instructions that it implied. Note Although PE execution has also canceled execution of the STR instruction, the trace analyzer is unaware of this, because the STR instruction was never traced. This is because no P0 elements were generated that would indicate execution of the STR instruction. The data fault exception occurred at 0x2004 . The Exception element indicates the MOV instruction at 0x2000 was executed. In summary: 1. The MOV instruction was first implied by theN Atom element at 0x200C . However, the trace analyzer canceled this because of the Cancel element . 2. The MOV instruction is now implied by the |
|        |                                               |                                                             | Exception element .                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|        | IRQ                                           | address( 0x4000 ) exception(IRQ, 0x4000 )                   | This Exception element contains the address of the exception vector of the DataFault exception. This implies that no instructions have executed since the DataFault exception.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |

| Execution            | Trace elements   | Notes                                                                                                                                                                                                                           |
|----------------------|------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| commit all execution | commit(3)        | This commits the E Atom element that was generated for the Branch instruction at 0x1000 , plus the Exception element generated for the Data fault exception and the Exception element that was generated for the IRQ exception. |

## K10.5.8.2 Examples of changes in context

When the PE executes an instruction that changes the execution context, the exact time at which the new element is traced depends on the PE operation after the write. An example of an instruction that changes the execution context is an instruction that writes a value to the CONTEXTIDR\_EL1. See Context element for more information about the rules controlling the generation of Context elements. This section provides examples of PE trace that contain changes of execution context to illustrate these rules. This section is split into the following:

- Exception in software executed after context synchronization.
- Exception immediately after ISB.
- Exception immediately before ISB.

Table K10-11 shows a write to the CONTEXTIDR\_EL1 register, followed by an ISB to synchronize that write, followed by an exception that changes the context again.

Table K10-11 Program trace containing a context changing operation

|        | Execution      | Context      | Trace elements                                                    | Notes                                                                                                                                                                                                                                                                                                                                                |
|--------|----------------|--------------|-------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0x1000 | B-> 0x2000     | 0xAA         | trace_info() trace_on() context( 0xAA ) address( 0x1000 ) atom(E) | Tracing begins here, therefore the trace unit must generate both: -A Context element . -A Target Address element . The instruction executed is a taken branch, so in addition, the trace unit must generate an E Atom element .                                                                                                                      |
| 0x2000 | MSR CONTEXTIDR | 0xAA         |                                                                   | None of these instructions are traced as P0 elements , therefore no trace elements are generated. The instructions might be executed from context 0xAA or 0xBB but they are always traced as occurring from context 0xAA .                                                                                                                           |
| 0x2004 | ADD            | 0xAA or 0xBB |                                                                   |                                                                                                                                                                                                                                                                                                                                                      |
| 0x2008 | ISB            | 0xAA or 0xBB | atom(E)                                                           | The trace unit generates an E Atom element , because the ISB is a Context synchronization event. All execution is traced as executing in context 0xAA .                                                                                                                                                                                              |
| 0x200C | SUB            | 0xBB         | context( 0xBB )                                                   | A Context element is traced to indicate the new context.                                                                                                                                                                                                                                                                                             |
|        | IRQ            | 0xBB         | exception(IRQ, 0x2010 )                                           | An IRQ exception occurs. The trace unit generates an Exception element .                                                                                                                                                                                                                                                                             |
| 0x3000 | B -> 0x4000    | 0xCC         | context( 0xCC ) address( 0x3000 ) atom(E)                         | A Context element is traced to indicate the new context. A Target Address element is also traced, because an Exception element is always followed by a Target Address element to indicate the address that the exception has been taken to. Finally, the instruction executed is a taken branch, so the trace unit must generate an E Atom element . |

ILSZCM

Table K10-12 shows the same execution as Table K10-11 but the exception occurs one instruction earlier. This means that no execution takes place between the ISB and the exception.

IRWRWJ

IGCRKW

Table K10-12 Program trace containing a context changing operation (exception immediately after ISB)

|        | Execution      | Context      | Trace elements                                                    | Notes                                                                                                                                                                                                                                                                                                                                                |
|--------|----------------|--------------|-------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0x1000 | B-> 0x2000     | 0xAA         | trace_info() trace_on() context( 0xAA ) address( 0x1000 ) atom(E) | Tracing begins here, therefore the trace unit must generate both: -A Context element . -A Target Address element . The instruction executed is a taken branch, so in addition, the trace unit must generate an E Atom element .                                                                                                                      |
| 0x2000 | MSR CONTEXTIDR | 0xAA         |                                                                   | None of these instructions are traced as P0 elements , therefore no trace elements are generated. The instructions might be executed from context 0xAA or 0xBB but they are always traced as occurring from context 0xAA .                                                                                                                           |
| 0x2004 | ADD            | 0xAA or 0xBB |                                                                   |                                                                                                                                                                                                                                                                                                                                                      |
| 0x2008 | ISB            | 0xAA or 0xBB | atom(E)                                                           | The trace unit generates an E Atom element , because the ISB is a Context synchronization event. All execution is traced as executing in context 0xAA .                                                                                                                                                                                              |
|        | IRQ            | 0xBB         | context( 0xBB ) exception(IRQ, 0x200C )                           | A Context element is traced to indicate the new context. An IRQ exception occurs. The trace unit generates an Exception element .                                                                                                                                                                                                                    |
| 0x3000 | B -> 0x4000    | 0xCC         | context( 0xCC ) address( 0x3000 ) atom(E)                         | A Context element is traced to indicate the new context. A Target Address element is also traced, because an Exception element is always followed by a Target Address element to indicate the address that the exception has been taken to. Finally, the instruction executed is a taken branch, so the trace unit must generate an E Atom element . |

IPDLNN

Table K10-13 is the same as Table K10-12 but the exception occurs one instruction earlier. This means that the exception occurs before the ISB instruction that was present in previous examples.

Table K10-13 Program trace containing a context changing operation (exception immediately before ISB)

|        | Execution      | Context      | Trace elements                                                    | Notes                                                                                                                                                                                                                                                                                                                                                |
|--------|----------------|--------------|-------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0x1000 | B-> 0x2000     | 0xAA         | trace_info() trace_on() context( 0xAA ) address( 0x1000 ) atom(E) | Tracing begins here, therefore the trace unit must generate both: -A Context element . -A Target Address element . The instruction executed is a taken branch, so in addition, the trace unit must generate an E Atom element .                                                                                                                      |
| 0x2000 | MSR CONTEXTIDR | 0xAA         |                                                                   | None of these instructions are traced as P0 elements , therefore no trace elements are generated. The instructions might be executed from context 0xAA or 0xBB but they are always traced as occurring from context 0xAA .                                                                                                                           |
| 0x2004 | ADD            | 0xAA or 0xBB |                                                                   |                                                                                                                                                                                                                                                                                                                                                      |
|        | IRQ            | 0xAA or 0xBB | exception(IRQ, 0x2008 )                                           | An IRQ exception occurs. The trace unit generates an Exception element .                                                                                                                                                                                                                                                                             |
| 0x3000 | B -> 0x4000    | 0xCC         | context( 0xCC ) address( 0x3000 ) atom(E)                         | A Context element is traced to indicate the new context. A Target Address element is also traced, because an Exception element is always followed by a Target Address element to indicate the address that the exception has been taken to. Finally, the instruction executed is a taken branch, so the trace unit must generate an E Atom element . |

IHRHBK

## K10.5.8.3 An example of the use of the trace unit return stack

This section contains two examples of tracing the same piece of program code. However:

- In the first example the trace unit return stack is disabled.
- In the second example trace unit the return stack is enabled.

The examples demonstrate that use of the trace unit return stack can help to reduce the amount of trace generated. Table K10-14 the first example, and Table K10-15 shows the second example. In these examples, the trace unit is programmed for basic program flow, where only branch instructions are traced as P0 instructions , and is programmed to start tracing when the instruction at 0x1000 is accessed.

Table K10-14 Basic program trace when Branch with Link instructions are executed and the return stack is disabled

|        | Execution                  | Trace elements                                              | Notes                                                                                                                                                                                                                                                                          |
|--------|----------------------------|-------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0x1000 | BL -> 0x2000               | trace_info() trace_on() context() address( 0x1000 ) atom(E) | Tracing begins here, therefore the trace unit must generate both: • A Context element . • An Target Address element . The instruction executed is a taken branch, so in addition, the trace unit must generate an E Atom element .                                             |
| 0x2000 | MOV                        |                                                             | None of these instructions are traced as P0 elements , therefore no trace elements are generated.                                                                                                                                                                              |
| 0x2004 | LDR                        |                                                             |                                                                                                                                                                                                                                                                                |
| 0x2008 | CMP                        |                                                             |                                                                                                                                                                                                                                                                                |
| 0x200C | BLEQ -> 0x3000 (not taken) |                                                             | This branch is not taken, so the trace unit generates anN Atom element . TheN Atom element implies the execution of the three previous instructions and the BLEQ instruction.                                                                                                  |
| 0x2010 | STR                        |                                                             |                                                                                                                                                                                                                                                                                |
| 0x2014 | BX LR                      | atom(E)                                                     | This branch is taken, so the trace unit generates an E Atom element . The E Atom element implies the execution of the STR and the BX instructions.                                                                                                                             |
| 0x1004 | MOV                        | address( 0x1004 )                                           | This instruction is not traced as a P0 element , therefore no trace element is generated. However, the last instruction executed was a taken indirect branch instruction, so the trace unit generates an Target Address element to indicate the target of that branch.         |
| 0x1008 | B -> 0x4000                | atom(E)                                                     | This branch is taken, so the trace unit generates an E Atom element . The E Atom element implies the execution of the MOV instruction at 0x1004 and the B instruction.                                                                                                         |
|        | commit all execution       | commit(4)                                                   | This commits all four of the following: • The E Atom element generated for the branch at 0x1000 . • TheN Atom element generated for the branch at 0x200C . • The E Atom element generated for the branch at 0x2014 . • The E Atom element generated for the branch at 0x1008 . |

IBQTVJ

Table K10-15 Basic program trace when Branch with Link instructions are executed and the return stack is enabled

|        | Execution                  | Trace elements                                              | Notes                                                                                                                                                                                                                                                                                                                                                                                          |
|--------|----------------------------|-------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0x1000 | BL -> 0x2000               | trace_info() trace_on() context() address( 0x1000 ) atom(E) | Tracing begins here, therefore the trace unit must generate both: • A Context element . • An Target Address element . The instruction executed is a taken branch, so in addition, the trace unit must generate an E Atom element . In addition, because the return stack is enabled, the Branch with Link instruction causes the address 0x1004 to be pushed onto the trace unit return stack. |
| 0x2000 | MOV                        |                                                             | None of these instructions are traced as P0 elements , therefore no trace elements are generated.                                                                                                                                                                                                                                                                                              |
| 0x2004 | LDR                        |                                                             |                                                                                                                                                                                                                                                                                                                                                                                                |
| 0x2008 | CMP                        |                                                             |                                                                                                                                                                                                                                                                                                                                                                                                |
| 0x200C | BLEQ -> 0x3000 (not taken) |                                                             | This branch is not taken, so the trace unit generates anN Atom element . TheN Atom element implies the execution of the three previous instructions and the BLEQ instruction. Nothing is pushed onto the trace unit return stack because the branch is not taken.                                                                                                                              |
| 0x2010 | STR                        |                                                             |                                                                                                                                                                                                                                                                                                                                                                                                |
| 0x2014 | BX LR                      | atom(E)                                                     | This branch is taken, so the trace unit generates an E Atom element . The E Atom element implies the execution of the STR and the BX instructions.                                                                                                                                                                                                                                             |
| 0x1004 | MOV                        |                                                             | This instruction is not traced as a P0 element , therefore no trace element is generated. The address of this instruction matches the top entry on the trace unit return stack. Therefore, the trace analyzer knows to restart program execution here and an Target Address element is not required. The top entry on the return stack, address 0x1004 , is popped from the return stack.      |
| 0x1008 | B -> 0x4000                | atom(E)                                                     | This branch is taken, so the trace unit generates an E Atom element . The E Atom element implies the execution of the MOV instruction at 0x1004 and the B instruction.                                                                                                                                                                                                                         |
|        | commit all execution       | commit(4)                                                   | This commits all four of the following: • The E Atom element generated for the branch at 0x1000 . • TheN Atom element generated for the branch at 0x200C . • The E Atom element generated for the branch at 0x2014 .                                                                                                                                                                           |

## K10.5.8.4 Transactions

The following is an example of a successful transaction traced by a trace unit with no speculation in the trace element stream.

Table K10-16 Example of trace with a successful transaction

|        | Execution   | Trace elements                                          | Notes                   |
|--------|-------------|---------------------------------------------------------|-------------------------|
| 0x1000 | B -> 0x2000 | Trace_info( . . . ) Trace_on() Target_address( 0x2000 ) | Trace on.               |
| 0x2000 | TSTART      | Atom(E) Transaction_start()                             | The transaction starts. |

|           | Execution   | Trace elements       | Notes                 |
|-----------|-------------|----------------------|-----------------------|
| 0x2004    | B -> 0x2400 | Atom(E)              |                       |
| { . . . } |             |                      |                       |
| 0x2804    | B -> 0x2808 | Atom(E)              |                       |
| 0x2808    | TCOMMIT     | Transaction_commit() | Transaction finishes. |
| { . . . } |             |                      |                       |

IGBKYZ

The following is an example of a failed transaction traced by a trace unit with no speculation in the trace element stream.

Table K10-17 Example of trace with a transaction failure

|           | Execution         | Trace elements                                                  | Notes                                                                  |
|-----------|-------------------|-----------------------------------------------------------------|------------------------------------------------------------------------|
| 0x2000    | TSTART            | Trace_on() Target_address( 0x2000 ) Atom(E) Transaction_start() | Trace on. The transaction starts.                                      |
| 0x2004    | TST               |                                                                 |                                                                        |
| 0x2008    | BEQ               | Atom(N)                                                         |                                                                        |
| { . . . } |                   |                                                                 |                                                                        |
| 0x2804    | B -> 0x3000       | Atom(E) Target_address( 0x3000 )                                |                                                                        |
|           | Transaction fails | Transaction_failure()                                           | Transaction fails.                                                     |
| 0x2004    | TST               | Target_address( 0x2004 )                                        | This address is where execution resumes after the transaction failure. |
| 0x2008    | BEQ               | Atom(E)                                                         |                                                                        |
| { . . . } |                   |                                                                 |                                                                        |

IFYFSF

The following is an example of trace with speculation in the trace element stream, and a failed transaction occurs. The speculative elements inside the transaction are cancelled using Cancel elements, and the transaction as a whole is indicated to have failed using a Transaction Failure element.

Table K10-18 Example of trace with a failed transaction

|           | Execution         | Trace elements                                                  | Notes                             |
|-----------|-------------------|-----------------------------------------------------------------|-----------------------------------|
| 0x2000    | TSTART            | Trace_on() Target_address( 0x2000 ) Atom(E) Transaction_start() | Trace on. The transaction starts. |
| 0x2004    | TST               |                                                                 |                                   |
| 0x2008    | BEQ               | Atom(N)                                                         |                                   |
| { . . . } |                   |                                                                 |                                   |
| 0x2804    | B -> 0x3000       | Atom(E)                                                         |                                   |
|           | Transaction fails | Target_address( 0x3000 ) Cancel(2) Transaction_failure()        | Transaction fails.                |
| 0x2004    | TST               | Target_address( 0x2004 )                                        |                                   |
| 0x2008    | BEQ               | Atom(E)                                                         |                                   |

| Execution   | Trace elements   | Notes   |
|-------------|------------------|---------|
| { . . . }   |                  |         |

ICRDGM

The following is an example of a transaction which is started speculatively and is traced using speculative trace elements, but that speculation is subsequently resolved as misspeculation. The Cancel elements are used to cancel execution back past the start of the transaction.

## Table K10-19 Example of trace with a transaction failure

|           | Execution   | Trace elements              | Notes                                                                                                                                                                                                                                                  |
|-----------|-------------|-----------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| { . . . } |             |                             |                                                                                                                                                                                                                                                        |
| 0x1000    | B -> 0x2000 | Atom(E)                     | This branch is speculatively taken, but was incorrectly speculated and will be corrected later.                                                                                                                                                        |
| 0x2000    | TSTART      | Atom(E) Transaction_start() | The transaction starts.                                                                                                                                                                                                                                |
| 0x2004    | TST         |                             |                                                                                                                                                                                                                                                        |
| 0x2008    | BEQ         | Atom(N)                     |                                                                                                                                                                                                                                                        |
| { . . . } |             |                             |                                                                                                                                                                                                                                                        |
| 0x2804    | B -> 0x3000 | Atom(E)                     |                                                                                                                                                                                                                                                        |
|           |             | Cancel(4) Mispredict        | The transaction was only speculatively started. It is optional if a Transaction Failure element is traced, because the Cancel element cancels the Transaction Start element . The Mispredict element corrects the incorrectly speculated first branch. |
| 0x1004    | { . . . }   |                             |                                                                                                                                                                                                                                                        |
| { . . . } |             |                             |                                                                                                                                                                                                                                                        |

## K10.5.9 Differences between ETM and ETE

IJNLFZ

ETE has a considerable overlap with the ETMv4 architecture, with the intent that broadly unified software stack can program a trace unit and interpret the trace stream from either an ETMv4 trace unit or an ETE trace unit.

This section describes the primary functional differences between ETMv4 and ETE.

- Removal of data trace documentation, since this is not permitted in A-profile.
- Removal of conditional non-branch documentation, since this is not permitted in A-profile.
- TRCDEVARCH.PRESENT == 1 is mandatory.
- TRCDEVARCH.ARCHVER and TRCDEVARCH.REVISION take new values.
- TRCIDR1.TRCARCHMAJ and TRCIDR1.TRCARCHMIN take new values.
- TRCIDR9 is fixed at zero.
- Context identifier tracing is mandatory, defined in TRCIDR2.CIDSIZE.
- Virtual context identifier tracing is mandatory when the PE implements EL2, defined in TRCIDR2.VMIDSIZE.
- The Virtual context identifier is always based on CONTEXTIDR\_EL2, with support for tracing VTTBR\_EL2.VMID removed.
- 64-bit timestamp is the only supported timestamp size.
- Timestamping is mandatory in ETE.
- TRCIDR2.IASIZE is only permitted to indicate a 64-bit instruction address size.
- External Inputs are unified with the PMU event space, with new TRCEXTINSELR&lt;n&gt; registers introduced.
- TRCIDR5.NUMEXTIN indicates the unified External Input model.
- Added TRCRSR.EXTIN for reading and setting the External Input Selectors state.

- Added TRCRSR.EVENT for reading and setting the ETEEvent state.
- Added TRCRSR.TA for reading and setting whether tracing was active.
- Changed requirements for the tracing of Exceptions to be dependent on the new TRCRSR.TA field.
- Removal of memory-mapped accesses. This was deprecated in ETMv4.4 for Armv8-A.
- Removal of trace unit sharing.
- Added a requirement that trace must be output within finite time.
- Added a requirement that the trace unit resources are paused when entering a Trace Prohibited region.
- Added a bit to TRCSSCSR&lt;n&gt; to indicate that the Single-shot Comparator Control fired while the resources are paused.
- Added requirements for dependencies on the TSB CSYNC instruction.
- Execution of TSB CSYNC instruction requests a timestamp element.
- The Unified Power Domain Model from ETMv4.5 for Armv8-A is mandatory in ETE.
- Changes to the enable and disable code sequences.
- Addition of the tracing of Transactional state.
- Tightened the requirements for obeying the order of start point and stop points for the ViewInst start/stop function, and tightened the rules for programming the start/stop function.
- Addition of Source Address elements .
- Added rules to require no trace to be generated in Trace Prohibited regions, under some circumstances.
- Added constraints for the effect of system instructions causing the trace unit to become enabled or disabled.
- Additional constraints for the forced tracing of exceptions around Trace Prohibited regions, to ensure trace is not generated in Trace Prohibited regions.
- Removed the flexibility around tracing of an Exceptional occurrence immediately after a Trace Prohibited region or when trace generation becomes operative. Such Exceptional occurrences are not traced.
- Added a requirement that the resource operations must complete before a TSB instruction completes.
- Defined the behavior of the visibility of reads and writes to trace unit registers from system instructions, external debugger and by the trace unit.
- Changed branch broadcasting to be required in all implementations, see TRCIDR0.TRCBB.
- TRCSYNCPR is read/write in all implementations, see TRCIDR3.SYNCPR.
- Forced tracing of System Error exceptions is required in all implementations, see TRCIDR3.TRCERR.
- Changed cycle counting to be required in all implementations, see TRCIDR0.TRCCCI.
- Removed the trace unit OS Lock mechanism, and changed to require the PE OS Lock to affect the trace unit.
- Removed the Exception Return element and Exception Return packet.
- Constrained TRCCLAIMCLR and TRCCLAIMSET to not require explicit synchronization.
- Added more constraints to the operation of the Single-shot Comparator Controls when the trace unit becomes disabled, or when entering a Trace Prohibited region.
- Added more constraints to the operation of the ViewInst start/stop function when the trace unit becomes disabled, or when entering a Trace Prohibited region.
- Constrained the behavior of cycle counting after a trace unit buffer overflow, to require the cycle count to be traced as UNKNOWN on the first Cycle Count element after an overflow.
- Export of PMU events to the trace unit is not affected by PMCR.X or PMCR\_EL0.X.
- Event elements are permitted to be generated before the first Trace Info element .

## K10.5.10 Context switching

SVKHHY

When switching out a process being traced, to save the current trace context and ensure all trace operations are written to the correct context:

1. Prohibit program-flow trace using TRFCR\_ELx. In many cases this is done before the process is traced. For example if all of the following are true:
- TRFCR\_EL1.E0TRE is 1 to allow tracing of a process executed at EL0.
- TRFCR\_EL1.E1TRE is 0 to prohibit tracing of the Operating System performing the context switch executed at EL1.
2. Execute a Context synchronization event to guarantee no new program-flow trace is generated. In the common case, this Context synchronization event is an exception taken to an Exception level where tracing is prohibited.
- If the trace unit is an ETE and the ETE is enabled, this also pauses the ETE Resources.
3. Execute a TSB CSYNC instruction to ensure the program-flow trace is flushed.

SFMBCL

SPKLXF

SYKCND

4. If necessary, disable the trace unit.
- For an ETE this is necessary if context is being switched. Software must set TRCPRGCTLR.EN to zero. This is necessary as:
3. -The ETE must be disabled if saving the ETE state, as the ETE System registers can only be read when the ETE is disabled.
4. -ETE trace compression logic is stateful, and disabling the ETE resets this compression state.
5. Disable the Trace Buffer Unit. Set TRBLIMITR\_EL1.E to zero.
- This must be done before changing the VMSA System registers to prevent the Trace Buffer Unit from speculatively accessing translation table entries.
6. Execute a DSB operation.
- This is required if software will be reading the trace buffer contents, to ensure the writes to memory are Complete.
7. Execute a further Context synchronization event.
- This is required to synchronize the effects of any System register writes since the previous Context synchronization event.
- This is also required if software will be reading the Trace Buffer Unit or trace unit System registers as part of the context switch, to capture indirect writes to those registers by trace operations synchronized by the TSB CSYNC .
- For a subsequent direct read to capture the indirect write to TRBSR\_EL1 resulting from an External abort on a completed write, this Context synchronization event must follow the DSB above.
8. Save and/or change the context. For example, save the MDCR\_EL3, MDCR\_EL2 (if applicable), Trace Buffer Unit, trace unit, and TRFCR\_ELx System registers, and update the VMSA System registers for the new process.

In other uses cases, tracing is not prohibited when software wants to save the trace context. For this case, if using an ETE, the sequence is slightly different:

1. Disable the ETE. Set TRCPRGCTLR.EN to zero.
2. Execute a Context synchronization event to guarantee no new program-flow trace is generated.
3. Execute a TSB CSYNC instruction to ensure the program-flow trace is flushed.
4. Execute a DSB and/or Context synchronization event as required by the previous example.
5. Save and/or change the context.

For an ETE this sequence does not guarantee that all instructions before disabling the ETE are traced. The ETE might discard trace for preceding instructions when it is disabled.

To restore the state of the Trace Buffer Unit and trace unit for switching in a process being traced, while tracing is prohibited:

1. Restore the context. For example:
- Restore MDCR\_EL3, MDCR\_EL2 (if applicable), and the Trace Buffer Unit System registers, other than TRBLIMITR\_EL1.
- Restore the trace unit System registers, other than enabling the trace unit.
- Ensure the TRFCR\_ELx System registers are correct for the process being traced.
- Update VMSA System registers for the process being returned to.
2. Execute a Context synchronization event to guarantee the trace unit and Trace Buffer Unit will observe the new values of the System registers written by the previous step.
3. Enable the Trace Buffer Unit by setting TRBLIMITR\_EL1.E to 1. This must be done after setting up the correct VMSASystem registers for the trace buffer, as the Trace Buffer Unit might now speculatively prefetch and cache address translations. See RBSMLW and SYKCND.
4. If necessary, enable the trace unit. If using an ETE, software must set TRCPRGCTLR.EN to one.
5. Execute a Context synchronization event to guarantee tracing is allowed. In the common case, this is an ERET instruction that returns to a different Exception level where tracing is allowed.

This must be done after saving the state from the previous process, if applicable.

Because the Trace Buffer Unit can prefetch and cache address translations when the Trace Buffer Unit is enabled:

- Software must not enable the Trace Buffer Unit before programming the System registers for the owning translation regime. In particular, during a context switch operation:
- -If switching from a context using the Trace Buffer Unit, the Trace Buffer Unit must be disabled before modifying the System registers for the owning translation regime being switched from.
- -If switching to a context using the Trace Buffer Unit, the Trace Buffer Unit must not be enabled until after modifying the System registers for the owning translation regime being switched to.

- The Trace Buffer Unit must not be enabled when the PE is not executing in the owning Security state or when executing at EL3 and SCR\_EL3.NS does not indicate the owning Security state.
- In normal conditions, enabling the Trace Buffer Unit early before returning to the context being traced might be advantageous if the implementation does prefetch address translations.

## K10.5.11 Controlling generation of trace buffer management events

SNFQZJ

The TRBE does not include a direct capability to program the Trace Buffer Unit to generate a maintenance interrupt when the trace buffer reaches a programmed level below the Limit pointer, and continue collecting trace until either the interrupt is serviced or (possibly) the trace buffer fills (whichever comes first). This allows an almost lossless collection of trace.

However, the Trace Buffer Unit can be programmed to give similar behavior in one of the following ways:

1. Using Wrap mode. At the start of a trace session, configure the Base pointer and Limit pointer for the trace buffer as normal, but set the trace buffer mode to Wrap mode the current write pointer to point part way through the trace buffer, such that the remaining space in the trace buffer is the watermark level. When the amount of trace collected reaches the watermark level, the current write pointer is wrapped and a trace buffer management event is generated, but trace continues to be collected. This approach has the following advantages and disadvantages:
- The trace buffer management event is generated and the trace unit receives the TRB\_WRAP event at the watermark level.
- The oldest trace in the trace buffer will be lost if more trace is generated than fits in the trace buffer, because it is overwritten by newer trace. Note that some loss of trace is inevitable if more trace is generated than fits in the trace buffer.
- The trace history does not start at the start of the trace buffer, and must be aligned by software.
2. Use a Trigger Event . At the start of a trace session, configure the Base pointer and Limit pointer for the trace buffer as normal, and set the trace buffer mode to Fill mode and the current write pointer to the start of the trace buffer. Set the trigger mode to IRQ on trigger , the Trigger Counter to the watermark level, and TRBSR\_EL1.TRG to 1. When the amount of trace collected reaches the watermark level, a Trigger Event occurs and a trace buffer management event is generated, but trace continues to be collected. This approach has the following advantages and disadvantages:
- The trace buffer management event is generated and the trace unit receives the TRB\_TRIG event at the watermark level.
- The newest trace in the trace buffer will be discarded if more trace is generated than fits in the trace buffer. To overwrite the oldest trace instead, set the trace buffer mode to Circular Buffer mode.
- This method cannot be used if also searching for a Detected Trigger event from the trace unit.
- The current write pointer does not have to be set to the start of the trace buffer. If the trace buffer already contains data that software does not want to be overwritten, the current write pointer can be set to point to after this data. In this case using Circular Buffer mode or Stop on trigger can also be used to control when collection is stopped and what data is overwritten.