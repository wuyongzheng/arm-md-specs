## D5.3 Alphabetical list of ETE packets

This section lists each ETE packet and their description.

## D5.3.1 Alignment Synchronization Packet

## Purpose

Identifies a packet boundary.

All.

This packet forms a unique bit and byte pattern. Searching for this pattern allows the trace analyzer to identify packet boundaries.

## Packet Layout

## Additional information

For more information about the decoding of this packet see Parse\_ExtensionPacket().

For more information about the generation of this packet see Trace protocol synchronization.

RBXZZJ

Any byte that follows this unique sequence of bits is the header byte of a new packet.

RVRKLP

This packet must be output before the first Trace Info packet.

## Configurations

Figure D5-1 Alignment Synchronization Packet

## D5.3.2 Atom Format 1 Packet

## Purpose

Configurations

Indicates one Atom element .

All.

Packet Layout

## Field descriptions

A

Indicates a single Atom element .

The encoding for this field is POD.

| A   | Description        |
|-----|--------------------|
| 0b0 | OneN Atom element  |
| 0b1 | One E Atom element |

## Additional information

For more information about the decoding of this packet see AtomFormat1Packet().

For more information about the generation of this packet see Atom packing.

Figure D5-2 Atom Format 1 Packet

<!-- image -->

## D5.3.3 Atom Format 2 Packet

## Purpose

Configurations

Indicates two Atom elements .

All.

Packet Layout

## Field descriptions

A

Indicates a specific sequence of Atom elements .

The encoding for this field is POD.

| A    | Description                             |
|------|-----------------------------------------|
| 0b00 | 1. N Atom element . 2. N Atom element . |
| 0b01 | 1. E Atom element . 2. N Atom element . |
| 0b10 | 1. N Atom element . 2. E Atom element . |
| 0b11 | 1. E Atom element . 2. E Atom element . |

## Additional information

For more information about the decoding of this packet see AtomFormat2Packet().

For more information about the generation of this packet see Atom packing.

Figure D5-3 Atom Format 2 Packet

<!-- image -->

## D5.3.4 Atom Format 3 Packet

Purpose

Configurations

Indicates three Atom elements .

All.

Packet Layout

## Field descriptions

A

Indicates a specific sequence of Atom elements .

The encoding for this field is POD.

Figure D5-4 Atom Format 3 Packet

| A     | Description                                                 |
|-------|-------------------------------------------------------------|
| 0b000 | 1. N Atom element . 2. N Atom element .                     |
| 0b001 | 1. E Atom element . 2. N Atom element .                     |
| 0b010 | 1. N Atom element . 2. E Atom element . 3. N Atom element . |
| 0b011 | 1. E Atom element . 2. E Atom element .                     |
| 0b100 | 1. N Atom element . 2. N Atom element .                     |
| 0b101 | 1. E Atom element . 2. N Atom element . 3. E Atom element . |

<!-- image -->

| A     | Description                                                 |
|-------|-------------------------------------------------------------|
| 0b110 | 1. N Atom element . 2. E Atom element . 3. E Atom element . |
| 0b111 | 1. E Atom element . 2. E Atom element . 3. E Atom element . |

## Additional information

For more information about the decoding of this packet see AtomFormat3Packet().

For more information about the generation of this packet see Atom packing.

## D5.3.5 Atom Format 4 Packet

## Purpose

Configurations

Indicates four Atom elements .

All.

Packet Layout

## Field descriptions

A

Indicates a specific sequence of Atom elements .

The encoding for this field is POD.

| A    | Description                                                                     |
|------|---------------------------------------------------------------------------------|
| 0b00 | 1. N Atom element . 2. E Atom element . 3. E Atom element . 4. E Atom element . |
| 0b01 | 1. N Atom element . 2. N Atom element . 3. N Atom element . 4. N Atom element . |
| 0b10 | 1. N Atom element . 2. E Atom element . 3. N Atom element .                     |
| 0b11 | 1. E Atom element . 2. N Atom element . 3. E Atom element .                     |

## Additional information

For more information about the decoding of this packet see AtomFormat4Packet().

For more information about the generation of this packet see Atom packing.

Figure D5-5 Atom Format 4 Packet

<!-- image -->

## D5.3.6 Atom Format 5.1 Packet

## Purpose

Indicates five Atom elements .

All.

Packet Layout

## Element sequence

This packet encodes the following sequence:

1. N Atom element .
2. E Atom element .
3. E Atom element .
4. E Atom element .
5. E Atom element .

## Additional information

For more information about the decoding of this packet see AtomFormat5\_1Packet().

For more information about the generation of this packet see Atom packing.

Configurations

Figure D5-6 Atom Format 5.1 Packet

<!-- image -->

## D5.3.7 Atom Format 5.2 Packet

## Purpose

Indicates five Atom elements .

All.

Packet Layout

## Field descriptions

A

Indicates a specific sequence of Atom elements .

The encoding for this field is POD.

| A    | Description                                                                                         |
|------|-----------------------------------------------------------------------------------------------------|
| 0b01 | 1. N Atom element . 2. N Atom element . 3. N Atom element . 4. N Atom element . 5. N Atom element . |
| 0b10 | 1. N Atom element . 2. E Atom element . 3. N Atom element . 4. E Atom element . 5. N Atom element . |
| 0b11 | 1. E Atom element . 2. N Atom element . 3. E Atom element . 4. N Atom element .                     |

## Additional information

For more information about the decoding of this packet see AtomFormat5\_2Packet().

For more information about the generation of this packet see Atom packing.

Configurations

Figure D5-7 Atom Format 5.2 Packet

<!-- image -->

## D5.3.8 Atom Format 6 Packet

## Purpose

## Configurations

Indicates 3-23 E Atom elements , plus a subsequent E Atom or N Atom element .

All.

## Packet Layout

## Field descriptions

A

Indicates an E Atom element or N Atom element , after the E Atom elements indicated by COUNT. The encoding for this field is POD.

| A   | Description        |
|-----|--------------------|
| 0b0 | One E Atom element |
| 0b1 | OneN Atom element  |

## COUNT

Figure D5-8 Atom Format 6 Packet

<!-- image -->

Indicates a number of E Atom elements . The number is 3 + COUNT. Permitted values of COUNT are 0b00000 to 0b10100.

The encoding for this field is POD.

## Additional information

For more information about the decoding of this packet see AtomFormat6Packet().

For more information about the generation of this packet see Atom packing.

## D5.3.9 Commit Packet

## Purpose

Configurations

Indicates a Commit element .

TRCIDR8.MAXSPEC &gt; 0.

## Packet Layout

Field descriptions

C0

Continuation Bit.

The encoding for this field is Unary code.

| C0   | Description                                     |
|------|-------------------------------------------------|
| 0b0  | Last byte in this section.                      |
| 0b1  | At least one more byte follows in this section. |

## COMMIT

The number of P0 elements to be resolved.

The encoding for this field is unsigned LE128n.

## Element sequence

This packet encodes the following sequence:

1. Commit element .

## Additional information

For more information about the decoding of this packet see CommitPacket().

<!-- image -->

| 䌰        | 䍏䵍䥔嬶㨰    | 䍏䵍䥔嬶㨰    | 䍏䵍䥔嬶㨰    | 䍏䵍䥔嬶㨰   | 䍏䵍䥔嬶㨰   | 䍏䵍䥔嬶㨰   |
|----------|----------|----------|----------|---------|---------|---------|
| 䌰        | 䍏䵍䥔嬱㌺㝝   | 䍏䵍䥔嬱㌺㝝   | 䍏䵍䥔嬱㌺㝝   | 䍏䵍䥔嬱㌺㝝  | 䍏䵍䥔嬱㌺㝝  | 䍏䵍䥔嬱㌺㝝  |
| 䌰        | 䍏䵍䥔嬲〺ㄴ   | 䍏䵍䥔嬲〺ㄴ   | 䍏䵍䥔嬲〺ㄴ   | 䍏䵍䥔嬲〺ㄴ  | 䍏䵍䥔嬲〺ㄴ  | 䍏䵍䥔嬲〺ㄴ  |
| 䌰        | 䍏䵍䥔嬲㜺㈱   | 䍏䵍䥔嬲㜺㈱   | 䍏䵍䥔嬲㜺㈱   | 䍏䵍䥔嬲㜺㈱  | 䍏䵍䥔嬲㜺㈱  | 䍏䵍䥔嬲㜺㈱  |
| ⠰⤠⠰⤠⠰⤠⠰⤠ | ⠰⤠⠰⤠⠰⤠⠰⤠ | ⠰⤠⠰⤠⠰⤠⠰⤠ | ⠰⤠⠰⤠⠰⤠⠰⤠ | 䍏䵍䥔嬳ㄺ㈸  |         |         |

Figure D5-9 Commit Packet

## D5.3.10 Context Packet

Purpose

Configurations

All.

Packet Layout - Variant 1

## Packet Layout - Variant 2

Packet Layout - Variant 3

Indicates a Context element .

<!-- image -->

| 乓   | 卆   | 乓   | ⠰⤠   | 䕌   |
|-----|-----|-----|------|-----|

Figure D5-10 Context Packet (1)

Figure D5-11 Context Packet (2)

<!-- image -->

Figure D5-12 Context Packet (3)

<!-- image -->

|       | 乓     | 卆     | 乓     | ⠰⤠    | 䕌     |       |
|-------|-------|-------|-------|-------|-------|-------|
| 噍䥄嬷㨰  | 噍䥄嬷㨰  | 噍䥄嬷㨰  | 噍䥄嬷㨰  | 噍䥄嬷㨰  | 噍䥄嬷㨰  | 噍䥄嬷㨰  |
| 噍䥄嬱㔺㡝 | 噍䥄嬱㔺㡝 | 噍䥄嬱㔺㡝 | 噍䥄嬱㔺㡝 | 噍䥄嬱㔺㡝 | 噍䥄嬱㔺㡝 | 噍䥄嬱㔺㡝 |
| 噍䥄嬲㌺ㄶ | 噍䥄嬲㌺ㄶ | 噍䥄嬲㌺ㄶ | 噍䥄嬲㌺ㄶ | 噍䥄嬲㌺ㄶ | 噍䥄嬲㌺ㄶ | 噍䥄嬲㌺ㄶ |
| 噍䥄嬳ㄺ㈴ | 噍䥄嬳ㄺ㈴ | 噍䥄嬳ㄺ㈴ | 噍䥄嬳ㄺ㈴ | 噍䥄嬳ㄺ㈴ | 噍䥄嬳ㄺ㈴ | 噍䥄嬳ㄺ㈴ |

## Packet Layout - Variant 4

## Field descriptions

## CONTEXTID

Context identifier.

When this field is not output, the Context identifier is the same as the most recently output Context identifier.

If Context identifier tracing is disabled, then one of the following must occur:

- This field is not traced.
- This field contains a value of zero.

The encoding for this field is POD.

See Context identifier tracing.

Exception level.

The encoding for this field is POD.

| EL   | Description   |
|------|---------------|
| 0b00 | EL0           |
| 0b01 | EL1           |
| 0b10 | EL2           |
| 0b11 | EL3           |

NS

EL

Security state.

The encoding for this field is POD.

With the NSE bit, indicates the Security state associated with the address.

Figure D5-13 Context Packet (4)

|          | 乓        | 卆        | 乓        | 䕌        |          |          |
|----------|----------|----------|----------|----------|----------|----------|
| 噍䥄嬷㨰     | 噍䥄嬷㨰     | 噍䥄嬷㨰     | 噍䥄嬷㨰     | 噍䥄嬷㨰     | 噍䥄嬷㨰     | 噍䥄嬷㨰     |
| 噍䥄嬱㔺㡝    | 噍䥄嬱㔺㡝    | 噍䥄嬱㔺㡝    | 噍䥄嬱㔺㡝    | 噍䥄嬱㔺㡝    | 噍䥄嬱㔺㡝    | 噍䥄嬱㔺㡝    |
| 噍䥄嬲㌺ㄶ    | 噍䥄嬲㌺ㄶ    | 噍䥄嬲㌺ㄶ    | 噍䥄嬲㌺ㄶ    | 噍䥄嬲㌺ㄶ    | 噍䥄嬲㌺ㄶ    | 噍䥄嬲㌺ㄶ    |
| 噍䥄嬳ㄺ㈴    | 噍䥄嬳ㄺ㈴    | 噍䥄嬳ㄺ㈴    | 噍䥄嬳ㄺ㈴    | 噍䥄嬳ㄺ㈴    | 噍䥄嬳ㄺ㈴    | 噍䥄嬳ㄺ㈴    |
| 䍏乔䕘呉䑛㜺そ  | 䍏乔䕘呉䑛㜺そ  | 䍏乔䕘呉䑛㜺そ  | 䍏乔䕘呉䑛㜺そ  | 䍏乔䕘呉䑛㜺そ  | 䍏乔䕘呉䑛㜺そ  | 䍏乔䕘呉䑛㜺そ  |
| 䍏乔䕘呉䑛ㄵ㨸  | 䍏乔䕘呉䑛ㄵ㨸  | 䍏乔䕘呉䑛ㄵ㨸  | 䍏乔䕘呉䑛ㄵ㨸  | 䍏乔䕘呉䑛ㄵ㨸  | 䍏乔䕘呉䑛ㄵ㨸  | 䍏乔䕘呉䑛ㄵ㨸  |
| 䍏乔䕘呉䑛㈳㨱㙝 | 䍏乔䕘呉䑛㈳㨱㙝 | 䍏乔䕘呉䑛㈳㨱㙝 | 䍏乔䕘呉䑛㈳㨱㙝 | 䍏乔䕘呉䑛㈳㨱㙝 | 䍏乔䕘呉䑛㈳㨱㙝 | 䍏乔䕘呉䑛㈳㨱㙝 |
| 䍏乔䕘呉䑛㌱㨲㑝 | 䍏乔䕘呉䑛㌱㨲㑝 | 䍏乔䕘呉䑛㌱㨲㑝 | 䍏乔䕘呉䑛㌱㨲㑝 | 䍏乔䕘呉䑛㌱㨲㑝 | 䍏乔䕘呉䑛㌱㨲㑝 | 䍏乔䕘呉䑛㌱㨲㑝 |

| NSE   | NS   | Description                                                                                      |
|-------|------|--------------------------------------------------------------------------------------------------|
| 0b0   | 0b0  | Secure state. This value is defined only if Secure state is implemented, and reserved otherwise. |
| 0b0   | 0b1  | Non-secure state.                                                                                |
| 0b1   | 0b0  | Root state. This value is defined only if FEAT_RME is implemented, and reserved otherwise.       |
| 0b1   | 0b1  | Realm state. This value is defined only if FEAT_RME is implemented, and reserved otherwise.      |

## NSE

Security state, for more information see the NS field.

The encoding for this field is POD.

SF

AArch64 state.

The encoding for this field is POD.

| SF   | Description                 |
|------|-----------------------------|
| 0b0  | The PE is in AArch32 state. |
| 0b1  | The PE is in AArch64 state. |

## VMID

Virtual context identifier.

When this field is not output, the Virtual context identifier is the same as the most recently output Virtual context identifier.

If Virtual context identifier tracing is disabled, then one of the following must occur:

- This field is not traced.
- This field contains a value of zero.

The encoding for this field is POD.

See Virtual context identifier tracing.

## Element sequence

This packet encodes the following sequence:

1. Context element .

## Additional information

For more information about the decoding of this packet see Parse\_ContextBytes().

## D5.3.11 Context Same Packet

Purpose

Configurations

Indicates a Context element .

All.

Packet Layout

## Element sequence

This packet encodes the following sequence:

1. Context element .

## Additional information

For more information about the decoding of this packet see Parse\_ContextBytes().

Figure D5-14 Context Same Packet

<!-- image -->

## D5.3.12 Cycle Count Format 1\_0 unknown count Packet

## Purpose

## Configurations

Indicates zero or one Commit elements followed by a Cycle Count element with an UNKNOWN cycle count value.

All the following conditions must be met:

- TRCIDR0.COMMOPT == 0b0.
- TRCIDR0.TRCCCI == 0b1.

## Packet Layout

## Field descriptions

C0

Continuation Bit.

The encoding for this field is Unary code.

| C0   | Description                                     |
|------|-------------------------------------------------|
| 0b0  | Last byte in this section.                      |
| 0b1  | At least one more byte follows in this section. |

## COMMIT

Figure D5-15 Cycle Count Format 1\_0 unknown count Packet

| 䌰        | 䍏䵍䥔嬶㨰    | 䍏䵍䥔嬶㨰    | 䍏䵍䥔嬶㨰    | 䍏䵍䥔嬶㨰   | 䍏䵍䥔嬶㨰   |
|----------|----------|----------|----------|---------|---------|
| 䌰        | 䍏䵍䥔嬱㌺㝝   | 䍏䵍䥔嬱㌺㝝   | 䍏䵍䥔嬱㌺㝝   | 䍏䵍䥔嬱㌺㝝  | 䍏䵍䥔嬱㌺㝝  |
| 䌰        | 䍏䵍䥔嬲〺ㄴ   | 䍏䵍䥔嬲〺ㄴ   | 䍏䵍䥔嬲〺ㄴ   | 䍏䵍䥔嬲〺ㄴ  | 䍏䵍䥔嬲〺ㄴ  |
| 䌰        | 䍏䵍䥔嬲㜺㈱   | 䍏䵍䥔嬲㜺㈱   | 䍏䵍䥔嬲㜺㈱   | 䍏䵍䥔嬲㜺㈱  | 䍏䵍䥔嬲㜺㈱  |
| ⠰⤠⠰⤠⠰⤠⠰⤠ | ⠰⤠⠰⤠⠰⤠⠰⤠ | ⠰⤠⠰⤠⠰⤠⠰⤠ | ⠰⤠⠰⤠⠰⤠⠰⤠ |         |         |

If this field is zero, there is no Commit element . Otherwise, there is a Commit element before the Cycle Count element and this field indicates the number of P0 elements committed by the Commit element .

The encoding for this field is unsigned LE128n.

## Element sequence

This packet encodes the following sequence:

1. Commit element .
2. Cycle Count element with an unknown cycle count.

## Additional information

For more information about the decoding of this packet see CycleCountFormat1Packet().

## D5.3.13 Cycle Count Format 1\_0 with count Packet

## Purpose

## Configurations

Indicates zero or one Commit elements followed by a Cycle Count element .

All the following conditions must be met:

- TRCIDR0.COMMOPT == 0b0.
- TRCIDR0.TRCCCI == 0b1.

## Packet Layout

## Field descriptions

C0

Continuation Bit.

The encoding for this field is Unary code.

| C0   | Description                                     |
|------|-------------------------------------------------|
| 0b0  | Last byte in this section.                      |
| 0b1  | At least one more byte follows in this section. |

C1

Continuation Bit.

The encoding for this field is Unary code.

| C1   | Description                                     |
|------|-------------------------------------------------|
| 0b0  | Last byte in this section.                      |
| 0b1  | At least one more byte follows in this section. |

Figure D5-16 Cycle Count Format 1\_0 with count Packet

| 䌰        | 䍏䵍䥔嬶㨰    | 䍏䵍䥔嬶㨰    | 䍏䵍䥔嬶㨰    | 䍏䵍䥔嬶㨰   | 䍏䵍䥔嬶㨰   | 䍏䵍䥔嬶㨰   |
|----------|----------|----------|----------|---------|---------|---------|
| 䌰        | 䍏䵍䥔嬱㌺㝝   | 䍏䵍䥔嬱㌺㝝   | 䍏䵍䥔嬱㌺㝝   | 䍏䵍䥔嬱㌺㝝  | 䍏䵍䥔嬱㌺㝝  | 䍏䵍䥔嬱㌺㝝  |
| 䌰        | 䍏䵍䥔嬲〺ㄴ   | 䍏䵍䥔嬲〺ㄴ   | 䍏䵍䥔嬲〺ㄴ   | 䍏䵍䥔嬲〺ㄴ  | 䍏䵍䥔嬲〺ㄴ  | 䍏䵍䥔嬲〺ㄴ  |
| 䌰        | 䍏䵍䥔嬲㜺㈱   | 䍏䵍䥔嬲㜺㈱   | 䍏䵍䥔嬲㜺㈱   | 䍏䵍䥔嬲㜺㈱  | 䍏䵍䥔嬲㜺㈱  | 䍏䵍䥔嬲㜺㈱  |
| ⠰⤠⠰⤠⠰⤠⠰⤠ | ⠰⤠⠰⤠⠰⤠⠰⤠ | ⠰⤠⠰⤠⠰⤠⠰⤠ | ⠰⤠⠰⤠⠰⤠⠰⤠ | 䍏䵍䥔嬳ㄺ㈸  | 䍏䵍䥔嬳ㄺ㈸  |         |
| 䌱        | 䍏啎呛㘺そ    | 䍏啎呛㘺そ    | 䍏啎呛㘺そ    | 䍏啎呛㘺そ   | 䍏啎呛㘺そ   | 䍏啎呛㘺そ   |
| 䌱        | 䍏啎呛ㄳ㨷    | 䍏啎呛ㄳ㨷    | 䍏啎呛ㄳ㨷    | 䍏啎呛ㄳ㨷   | 䍏啎呛ㄳ㨷   | 䍏啎呛ㄳ㨷   |
| ⠰⤠⠰⤠     | ⠰⤠⠰⤠     | 䍏啎呛ㄹ㨱㑝   | 䍏啎呛ㄹ㨱㑝   | 䍏啎呛ㄹ㨱㑝  | 䍏啎呛ㄹ㨱㑝  | 䍏啎呛ㄹ㨱㑝  |

## COMMIT

## COUNT

If this field is zero, there is no Commit element . Otherwise, there is a Commit element before the Cycle Count element and this field indicates the number of P0 elements committed by the Commit element .

The encoding for this field is unsigned LE128n.

Indicates the number of PE clock cycles that have occurred between the 2 most recent Commit elements that both had a Cycle Count element associated with them. The cycle count is COUNT+cc\_threshold.

The encoding for this field is unsigned LE128n.

## Element sequence

This packet encodes the following sequence:

1. Commit element .
2. Cycle Count element .

## Additional information

For more information about the decoding of this packet see CycleCountFormat1Packet().

## D5.3.14 Cycle Count Format 1\_1 unknown count Packet

## Purpose

## Configurations

Indicates a Cycle Count element .

All the following conditions must be met:

- TRCIDR0.COMMOPT == 0b1.
- TRCIDR0.TRCCCI == 0b1.

## Packet Layout

## Element sequence

This packet encodes the following sequence:

1. Cycle Count element with an unknown cycle count.

## Additional information

For more information about the decoding of this packet see CycleCountFormat1Packet().

Figure D5-17 Cycle Count Format 1\_1 unknown count Packet

<!-- image -->

## D5.3.15 Cycle Count Format 1\_1 with count Packet

## Purpose

## Configurations

Indicates a Cycle Count element .

All the following conditions must be met:

- TRCIDR0.COMMOPT == 0b1.
- TRCIDR0.TRCCCI == 0b1.

## Packet Layout

## Field descriptions

C0

Continuation Bit.

The encoding for this field is Unary code.

| C0   | Description                                     |
|------|-------------------------------------------------|
| 0b0  | Last byte in this section.                      |
| 0b1  | At least one more byte follows in this section. |

## COUNT

Figure D5-18 Cycle Count Format 1\_1 with count Packet

| 䌰    | 䍏啎呛㘺そ   | 䍏啎呛㘺そ   | 䍏啎呛㘺そ   | 䍏啎呛㘺そ   | 䍏啎呛㘺そ   | 䍏啎呛㘺そ   |
|------|---------|---------|---------|---------|---------|---------|
| 䌰    | 䍏啎呛ㄳ㨷   | 䍏啎呛ㄳ㨷   | 䍏啎呛ㄳ㨷   | 䍏啎呛ㄳ㨷   | 䍏啎呛ㄳ㨷   | 䍏啎呛ㄳ㨷   |
| ⠰⤠⠰⤠ | ⠰⤠⠰⤠    | 䍏啎呛ㄹ㨱㑝  | 䍏啎呛ㄹ㨱㑝  | 䍏啎呛ㄹ㨱㑝  | 䍏啎呛ㄹ㨱㑝  | 䍏啎呛ㄹ㨱㑝  |

Indicates the number of PE clock cycles that have occurred between the 2 most recent Commit elements that both had a Cycle Count element associated with them. The cycle count is COUNT+cc\_threshold.

The encoding for this field is unsigned LE128n.

## Element sequence

This packet encodes the following sequence:

1. Cycle Count element .

## Additional information

For more information about the decoding of this packet see CycleCountFormat1Packet().

## D5.3.16 Cycle Count Format 2\_0 large commit Packet

## Purpose

## Configurations

## BBBB

Indicates the cycle value. The cycle count is calculated from cc\_threshold + BBBB. The encoding for this field is POD.

## Element sequence

This packet encodes the following sequence:

1. Commit element .
2. Cycle Count element .

## Additional information

For more information about the decoding of this packet see CycleCountFormat2Packet().

Indicates a Commit element and a Cycle Count element .

All the following conditions must be met:

- TRCIDR0.COMMOPT == 0b0.
- TRCIDR0.TRCCCI == 0b1.

## Packet Layout

## Field descriptions

## AAAA

Indicates the number of P0 elements to be resolved indicated by TRCIDR8.MAXSPEC + field - 15.

The number of P0 elements to be resolved must be greater than 0.

If the number of P0 elements to be resolved is less than 17 then it is preferred that a Cycle Count Format 2\_0 small commit Packet is used.

The encoding for this field is POD.

Figure D5-19 Cycle Count Format 2\_0 large commit Packet

<!-- image -->

## D5.3.17 Cancel Format 1 Packet

## Purpose

Indicates a Cancel element optionally followed by a Mispredict element .

TRCIDR8.MAXSPEC &gt; 0.

## Packet Layout

Field descriptions

C0

Continuation Bit.

The encoding for this field is Unary code.

| C0   | Description                                     |
|------|-------------------------------------------------|
| 0b0  | Last byte in this section.                      |
| 0b1  | At least one more byte follows in this section. |

## CANCEL

Configurations

The number of P0 elements to be canceled.

The encoding for this field is unsigned LE128n.

| CANCEL   | Description   |
|----------|---------------|
| 0b0      | Reserved      |

M

Mispredict element included in the packet.

The encoding for this field is POD.

Figure D5-20 Cancel Format 1 Packet

| 䌰        | 䍁乃䕌嬶㨰    | 䍁乃䕌嬶㨰    | 䍁乃䕌嬶㨰    | 䍁乃䕌嬶㨰   | 䍁乃䕌嬶㨰   | 䍁乃䕌嬶㨰   |
|----------|----------|----------|----------|---------|---------|---------|
| 䌰        | 䍁乃䕌嬱㌺㝝   | 䍁乃䕌嬱㌺㝝   | 䍁乃䕌嬱㌺㝝   | 䍁乃䕌嬱㌺㝝  | 䍁乃䕌嬱㌺㝝  | 䍁乃䕌嬱㌺㝝  |
| 䌰        | 䍁乃䕌嬲〺ㄴ   | 䍁乃䕌嬲〺ㄴ   | 䍁乃䕌嬲〺ㄴ   | 䍁乃䕌嬲〺ㄴ  | 䍁乃䕌嬲〺ㄴ  | 䍁乃䕌嬲〺ㄴ  |
| 䌰        | 䍁乃䕌嬲㜺㈱   | 䍁乃䕌嬲㜺㈱   | 䍁乃䕌嬲㜺㈱   | 䍁乃䕌嬲㜺㈱  | 䍁乃䕌嬲㜺㈱  | 䍁乃䕌嬲㜺㈱  |
| ⠰⤠⠰⤠⠰⤠⠰⤠ | ⠰⤠⠰⤠⠰⤠⠰⤠ | ⠰⤠⠰⤠⠰⤠⠰⤠ | ⠰⤠⠰⤠⠰⤠⠰⤠ | 䍁乃䕌嬳ㄺ㈸  |         |         |

| M   | Description                                            |
|-----|--------------------------------------------------------|
| 0b0 | No Mispredict element occurred                         |
| 0b1 | A Mispredict element occurred after the Cancel element |

## Additional information

For more information about the decoding of this packet see CancelFormat1Packet().

## D5.3.18 Cancel Format 2 Packet

## Purpose

Indicates zero or more E or N Atom elements followed by a Cancel element and a Mispredict element .

TRCIDR8.MAXSPEC &gt; 0.

## Packet Layout

## Field descriptions

A

Indicates the number of Atom elements that occurred before the Cancel element .

The encoding for this field is POD.

| A    | Description                                                                         |
|------|-------------------------------------------------------------------------------------|
| 0b00 | 1. Cancel element . 2. Mispredict element .                                         |
| 0b01 | 1. E Atom element . 2. Cancel element .                                             |
| 0b10 | 1. E Atom element . 2. E Atom element . 3. Cancel element . 4. Mispredict element . |
| 0b11 | 1. N Atom element . 2. Cancel element . 3. Mispredict element .                     |

## Additional information

For more information about the decoding of this packet see CancelFormat2Packet().

## Configurations

Figure D5-21 Cancel Format 2 Packet

<!-- image -->

## D5.3.19 Cancel Format 3 Packet

## Purpose

Indicates zero or one E Atom element followed by a Cancel element with a payload of 2-5 and one Mispredict element .

TRCIDR8.MAXSPEC &gt; 0.

## Packet Layout

## Field descriptions

A

Indicates the number of Atom elements that occurred before the Cancel element .

The encoding for this field is POD.

| A   | Description         |
|-----|---------------------|
| 0b0 | 1. Cancel element . |
| 0b1 | 1. E Atom element . |
|     | 2. Cancel element . |

CC

Configurations

The number of P0 elements to be canceled.

The encoding for this field is POD.

| CC   | Description          |
|------|----------------------|
| 0b00 | Cancel 2 P0 elements |
| 0b01 | Cancel 3 P0 elements |
| 0b10 | Cancel 4 P0 elements |
| 0b11 | Cancel 5 P0 elements |

## Additional information

For more information about the decoding of this packet see CancelFormat3Packet().

Figure D5-22 Cancel Format 3 Packet

<!-- image -->

## D5.3.20 Cycle Count Format 2\_0 small commit Packet

## Purpose

## Configurations

## BBBB

Indicates a Commit element and a Cycle Count element .

All the following conditions must be met:

- TRCIDR0.COMMOPT == 0b0.
- TRCIDR0.TRCCCI == 0b1.

## Packet Layout

## Field descriptions

## AAAA

Indicates the number of P0 elements to be resolved indicated by this field + 1.

The encoding for this field is POD.

Indicates the cycle value. The cycle count is calculated from cc\_threshold + BBBB.

The encoding for this field is POD.

## Element sequence

This packet encodes the following sequence:

1. Commit element .
2. Cycle Count element .

## Additional information

For more information about the decoding of this packet see CycleCountFormat2Packet().

Figure D5-23 Cycle Count Format 2\_0 small commit Packet

<!-- image -->

## D5.3.21 Cycle Count Format 2\_1 Packet

## Purpose

Indicates a Cycle Count element .

All the following conditions must be met:

- TRCIDR0.COMMOPT == 0b1.
- TRCIDR0.TRCCCI == 0b1.

## Packet Layout

## Field descriptions

## BBBB

Indicates the cycle value. The cycle count is calculated from cc\_threshold + BBBB.

The encoding for this field is POD.

## Element sequence

This packet encodes the following sequence:

1. Cycle Count element .

## Additional information

For more information about the decoding of this packet see CycleCountFormat2Packet().

## Configurations

Figure D5-24 Cycle Count Format 2\_1 Packet

<!-- image -->

| 䉂䉂   |
|------|

## D5.3.22 Cycle Count Format 3\_0 Packet

## Purpose

Indicates a Commit element and a Cycle Count element .

All the following conditions must be met:

- TRCIDR0.COMMOPT == 0b0.
- TRCIDR0.TRCCCI == 0b1.

## Packet Layout

## Field descriptions

AA

The number of P0 elements to be resolved indicated by this field + 1.

The encoding for this field is POD.

Indicates the cycle value. The cycle count is calculated from cc\_threshold + BB.

The encoding for this field is POD.

## Element sequence

This packet encodes the following sequence:

1. Commit element .
2. Cycle Count element .

## Additional information

For more information about the decoding of this packet see CycleCountFormat3Packet().

## Configurations

BB

Figure D5-25 Cycle Count Format 3\_0 Packet

<!-- image -->

## D5.3.23 Cycle Count Format 3\_1 Packet

## Purpose

Indicates a Cycle Count element .

All the following conditions must be met:

- TRCIDR0.COMMOPT == 0b1.
- TRCIDR0.TRCCCI == 0b1.

## Packet Layout

## Field descriptions

BB

Indicates the cycle value. The cycle count is calculated from cc\_threshold + BB.

The encoding for this field is POD.

## Element sequence

This packet encodes the following sequence:

1. Cycle Count element .

## Additional information

For more information about the decoding of this packet see CycleCountFormat3Packet().

## Configurations

Figure D5-26 Cycle Count Format 3\_1 Packet

<!-- image -->

## D5.3.24 Discard Packet

## Purpose

## Configurations

IRTFPP

Indicates a Discard element .

All.

Indicates a Discard element .

## Packet Layout

## Element sequence

This packet encodes the following sequence:

1. Discard element .

## Additional information

For more information about the decoding of this packet see DiscardPacket().

For more information about the generation of this packet see Trace protocol synchronization.

This packet is used to discard any speculative trace that the trace analyzer might still be holding onto.

Figure D5-27 Discard Packet

## D5.3.25 Event Packet

Purpose

Indicates 1-4 Event elements .

Configurations

All.

Packet Layout

嘳

嘲

嘱

嘰

Figure D5-28 Event Packet

Field descriptions

V0

Event 0 indicator.

The encoding for this field is POD.

<!-- image -->

| V0   | Description              |
|------|--------------------------|
| 0b0  | ETEEvent 0 did not occur |
| 0b1  | ETEEvent 0 occurred      |

V1

Event 1 indicator.

The encoding for this field is POD.

| V1   | Description              |
|------|--------------------------|
| 0b0  | ETEEvent 1 did not occur |
| 0b1  | ETEEvent 1 occurred      |

V2

Event 2 indicator.

The encoding for this field is POD.

| V2   | Description              |
|------|--------------------------|
| 0b0  | ETEEvent 2 did not occur |
| 0b1  | ETEEvent 2 occurred      |

V3

Event 3 indicator.

The encoding for this field is POD.

| V3   | Description              |
|------|--------------------------|
| 0b0  | ETEEvent 3 did not occur |
| 0b1  | ETEEvent 3 occurred      |

## Additional information

For more information about the decoding of this packet see EventTracingPacket().

Note

| [V3, V2, V1, V0] != 0b0000 as this is decoded as an Ignore Packet.   |
|----------------------------------------------------------------------|

## D5.3.26 Exception 32-bit Address IS0 Packet

## Purpose

Indicates that an exception has occurred.

Configurations

All.

Packet Layout

## Field descriptions

A

Preferred Exception Return address.

Preferred Exception Return address bits[1:0] always have the value 0b00.

The address is compressed relative to address history buffer entry 0.

The encoding for this field is Bit replacement.

Identifies the elements that are indicated by this packet.

The encoding for this field is POD.

| E    | Description                           |
|------|---------------------------------------|
| 0b01 | 1. Exception element (TYPE, ADDRESS). |
| 0b10 | 1. Target Address element (ADDRESS).  |
|      | 2. Exception element (TYPE, ADDRESS). |

All other values are reserved. Reserved values might be defined in a future version of the architecture.

The exception type.

The encoding for this field is POD.

E

TYPE

Figure D5-29 Exception 32-bit Address IS0 Packet

<!-- image -->

|      | 䕛ㅝ   | 䕛そ   |      |      |      |      |      |
|------|------|------|------|------|------|------|------|
| ⠰⤠   | 䅛㠺㉝  | 䅛㠺㉝  | 䅛㠺㉝  | 䅛㠺㉝  | 䅛㠺㉝  | 䅛㠺㉝  | 䅛㠺㉝  |
| ⠰⤠   | 䅛ㄵ㨹  | 䅛ㄵ㨹  | 䅛ㄵ㨹  | 䅛ㄵ㨹  | 䅛ㄵ㨹  | 䅛ㄵ㨹  | 䅛ㄵ㨹  |
| 䅛㈳㨱㙝 | 䅛㈳㨱㙝 | 䅛㈳㨱㙝 | 䅛㈳㨱㙝 | 䅛㈳㨱㙝 | 䅛㈳㨱㙝 | 䅛㈳㨱㙝 | 䅛㈳㨱㙝 |
| 䅛㌱㨲㑝 | 䅛㌱㨲㑝 | 䅛㌱㨲㑝 | 䅛㌱㨲㑝 | 䅛㌱㨲㑝 | 䅛㌱㨲㑝 | 䅛㌱㨲㑝 | 䅛㌱㨲㑝 |

| TYPE    | Description                               |
|---------|-------------------------------------------|
| 0b00000 | PE Reset, also see PE Reset Packet.       |
| 0b00001 | Debug halt.                               |
| 0b00010 | Call.                                     |
| 0b00011 | Trap.                                     |
| 0b00100 | System Error.                             |
| 0b00110 | Inst debug.                               |
| 0b00111 | Data debug.                               |
| 0b01010 | Alignment.                                |
| 0b01011 | Inst Fault.                               |
| 0b01100 | Data Fault.                               |
| 0b01110 | IRQ.                                      |
| 0b01111 | FIQ.                                      |
| 0b10000 | IMPLEMENTATION DEFINED 0.                 |
| 0b10001 | IMPLEMENTATION DEFINED 1.                 |
| 0b10010 | IMPLEMENTATION DEFINED 2.                 |
| 0b10011 | IMPLEMENTATION DEFINED 3.                 |
| 0b10100 | IMPLEMENTATION DEFINED 4.                 |
| 0b10101 | IMPLEMENTATION DEFINED 5.                 |
| 0b10110 | IMPLEMENTATION DEFINED 6.                 |
| 0b10111 | IMPLEMENTATION DEFINED 7.                 |
| 0b11000 | Reserved. See Transaction Failure Packet. |

All other values are reserved. Reserved values might be defined in a future version of the architecture.

## Additional information

For more information about the decoding of this packet see Parse\_ExceptionPacket().

For more information about the generation of this packet see Address compression.

For more information about the encoding of this packet see Instruction set encoding.

## D5.3.27 Exception 32-bit Address IS0 with Context Packet

Purpose

Configurations

Indicates that an exception has occurred.

All.

Packet Layout - Variant 1

Packet Layout - Variant 2

Figure D5-30 Exception 32-bit Address IS0 with Context Packet (1)

<!-- image -->

Figure D5-31 Exception 32-bit Address IS0 with Context Packet (2)

<!-- image -->

## Packet Layout - Variant 3

## Packet Layout - Variant 4

## Field descriptions

A

Preferred Exception Return address.

Preferred Exception Return address bits[1:0] always have the value 0b00.

The address is compressed relative to address history buffer entry 0.

The encoding for this field is Bit replacement.

Figure D5-32 Exception 32-bit Address IS0 with Context Packet (3)

<!-- image -->

|       | 䕛ㅝ    |       |       | 呙偅    |       | 䕛そ    |       |
|-------|-------|-------|-------|-------|-------|-------|-------|
| ⠰⤠    | 䅛㠺㉝   | 䅛㠺㉝   | 䅛㠺㉝   | 䅛㠺㉝   | 䅛㠺㉝   | 䅛㠺㉝   | 䅛㠺㉝   |
| ⠰⤠    | 䅛ㄵ㨹   | 䅛ㄵ㨹   | 䅛ㄵ㨹   | 䅛ㄵ㨹   | 䅛ㄵ㨹   | 䅛ㄵ㨹   | 䅛ㄵ㨹   |
| 䅛㈳㨱㙝  | 䅛㈳㨱㙝  | 䅛㈳㨱㙝  | 䅛㈳㨱㙝  | 䅛㈳㨱㙝  | 䅛㈳㨱㙝  | 䅛㈳㨱㙝  | 䅛㈳㨱㙝  |
| 䅛㌱㨲㑝  | 䅛㌱㨲㑝  | 䅛㌱㨲㑝  | 䅛㌱㨲㑝  | 䅛㌱㨲㑝  | 䅛㌱㨲㑝  | 䅛㌱㨲㑝  | 䅛㌱㨲㑝  |
|       |       | 乓     | 卆     | 乓     | ⠰⤠    | 䕌     |       |
| 噍䥄嬷㨰  | 噍䥄嬷㨰  | 噍䥄嬷㨰  | 噍䥄嬷㨰  | 噍䥄嬷㨰  | 噍䥄嬷㨰  | 噍䥄嬷㨰  | 噍䥄嬷㨰  |
| 噍䥄嬱㔺㡝 | 噍䥄嬱㔺㡝 | 噍䥄嬱㔺㡝 | 噍䥄嬱㔺㡝 | 噍䥄嬱㔺㡝 | 噍䥄嬱㔺㡝 | 噍䥄嬱㔺㡝 | 噍䥄嬱㔺㡝 |
| 噍䥄嬲㌺ㄶ | 噍䥄嬲㌺ㄶ | 噍䥄嬲㌺ㄶ | 噍䥄嬲㌺ㄶ | 噍䥄嬲㌺ㄶ | 噍䥄嬲㌺ㄶ | 噍䥄嬲㌺ㄶ | 噍䥄嬲㌺ㄶ |
| 噍䥄嬳ㄺ㈴ | 噍䥄嬳ㄺ㈴ | 噍䥄嬳ㄺ㈴ | 噍䥄嬳ㄺ㈴ | 噍䥄嬳ㄺ㈴ | 噍䥄嬳ㄺ㈴ | 噍䥄嬳ㄺ㈴ | 噍䥄嬳ㄺ㈴ |

Figure D5-33 Exception 32-bit Address IS0 with Context Packet (4)

<!-- image -->

|          | 䕛ㅝ       | 呙偅       |          |          |          | 䕛そ       |          |
|----------|----------|----------|----------|----------|----------|----------|----------|
| ⠰⤠       | 䅛㠺㉝      | 䅛㠺㉝      | 䅛㠺㉝      | 䅛㠺㉝      | 䅛㠺㉝      | 䅛㠺㉝      | 䅛㠺㉝      |
| ⠰⤠       | 䅛ㄵ㨹      | 䅛ㄵ㨹      | 䅛ㄵ㨹      | 䅛ㄵ㨹      | 䅛ㄵ㨹      | 䅛ㄵ㨹      | 䅛ㄵ㨹      |
| 䅛㈳㨱㙝     | 䅛㈳㨱㙝     | 䅛㈳㨱㙝     | 䅛㈳㨱㙝     | 䅛㈳㨱㙝     | 䅛㈳㨱㙝     | 䅛㈳㨱㙝     | 䅛㈳㨱㙝     |
| 䅛㌱㨲㑝     | 䅛㌱㨲㑝     | 䅛㌱㨲㑝     | 䅛㌱㨲㑝     | 䅛㌱㨲㑝     | 䅛㌱㨲㑝     | 䅛㌱㨲㑝     | 䅛㌱㨲㑝     |
|          |          | 乓        | 卆        | 乓        | ⠰⤠       | 䕌        |          |
| 噍䥄嬷㨰     | 噍䥄嬷㨰     | 噍䥄嬷㨰     | 噍䥄嬷㨰     | 噍䥄嬷㨰     | 噍䥄嬷㨰     | 噍䥄嬷㨰     | 噍䥄嬷㨰     |
| 噍䥄嬱㔺㡝    | 噍䥄嬱㔺㡝    | 噍䥄嬱㔺㡝    | 噍䥄嬱㔺㡝    | 噍䥄嬱㔺㡝    | 噍䥄嬱㔺㡝    | 噍䥄嬱㔺㡝    | 噍䥄嬱㔺㡝    |
| 噍䥄嬲㌺ㄶ    | 噍䥄嬲㌺ㄶ    | 噍䥄嬲㌺ㄶ    | 噍䥄嬲㌺ㄶ    | 噍䥄嬲㌺ㄶ    | 噍䥄嬲㌺ㄶ    | 噍䥄嬲㌺ㄶ    | 噍䥄嬲㌺ㄶ    |
| 噍䥄嬳ㄺ㈴    | 噍䥄嬳ㄺ㈴    | 噍䥄嬳ㄺ㈴    | 噍䥄嬳ㄺ㈴    | 噍䥄嬳ㄺ㈴    | 噍䥄嬳ㄺ㈴    | 噍䥄嬳ㄺ㈴    | 噍䥄嬳ㄺ㈴    |
| 䍏乔䕘呉䑛㜺そ  | 䍏乔䕘呉䑛㜺そ  | 䍏乔䕘呉䑛㜺そ  | 䍏乔䕘呉䑛㜺そ  | 䍏乔䕘呉䑛㜺そ  | 䍏乔䕘呉䑛㜺そ  | 䍏乔䕘呉䑛㜺そ  | 䍏乔䕘呉䑛㜺そ  |
| 䍏乔䕘呉䑛ㄵ㨸  | 䍏乔䕘呉䑛ㄵ㨸  | 䍏乔䕘呉䑛ㄵ㨸  | 䍏乔䕘呉䑛ㄵ㨸  | 䍏乔䕘呉䑛ㄵ㨸  | 䍏乔䕘呉䑛ㄵ㨸  | 䍏乔䕘呉䑛ㄵ㨸  | 䍏乔䕘呉䑛ㄵ㨸  |
| 䍏乔䕘呉䑛㈳㨱㙝 | 䍏乔䕘呉䑛㈳㨱㙝 | 䍏乔䕘呉䑛㈳㨱㙝 | 䍏乔䕘呉䑛㈳㨱㙝 | 䍏乔䕘呉䑛㈳㨱㙝 | 䍏乔䕘呉䑛㈳㨱㙝 | 䍏乔䕘呉䑛㈳㨱㙝 | 䍏乔䕘呉䑛㈳㨱㙝 |
| 䍏乔䕘呉䑛㌱㨲㑝 | 䍏乔䕘呉䑛㌱㨲㑝 | 䍏乔䕘呉䑛㌱㨲㑝 | 䍏乔䕘呉䑛㌱㨲㑝 | 䍏乔䕘呉䑛㌱㨲㑝 | 䍏乔䕘呉䑛㌱㨲㑝 | 䍏乔䕘呉䑛㌱㨲㑝 | 䍏乔䕘呉䑛㌱㨲㑝 |

## CONTEXTID

E

EL

Context identifier.

When this field is not output, the Context identifier is the same as the most recently output Context identifier.

If Context identifier tracing is disabled, then one of the following must occur:

- This field is not traced.
- This field contains a value of zero.

The encoding for this field is POD.

See Context identifier tracing.

Identifies the elements that are indicated by this packet.

The encoding for this field is POD.

| E    | Description                                                                                     |
|------|-------------------------------------------------------------------------------------------------|
| 0b01 | 1. Context element . 2. Exception element (TYPE, ADDRESS).                                      |
| 0b10 | 1. Target Address element (ADDRESS). 2. Context element . 3. Exception element (TYPE, ADDRESS). |

All other values are reserved. Reserved values might be defined in a future version of the architecture.

Exception level at the Preferred Exception Return address.

The encoding for this field is POD.

| EL   | Description   |
|------|---------------|
| 0b00 | EL0.          |
| 0b01 | EL1.          |
| 0b10 | EL2.          |
| 0b11 | EL3.          |

NS

Security state.

The encoding for this field is POD.

With the NSE bit, indicates the Security state associated with the address.

| NSE   | NS   | Description                                                                                      |
|-------|------|--------------------------------------------------------------------------------------------------|
| 0b0   | 0b0  | Secure state. This value is defined only if Secure state is implemented, and reserved otherwise. |
| 0b0   | 0b1  | Non-secure state.                                                                                |
| 0b1   | 0b0  | Root state. This value is defined only if FEAT_RME is implemented, and reserved otherwise.       |
| 0b1   | 0b1  | Realm state. This value is defined only if FEAT_RME is implemented, and reserved otherwise.      |

NSE

Security state, for more information see the NS field.

The encoding for this field is POD.

SF

AArch64 state.

The encoding for this field is POD.

| SF   | Description                 |
|------|-----------------------------|
| 0b0  | The PE is in AArch32 state. |
| 0b1  | The PE is in AArch64 state. |

TYPE

The exception type.

The encoding for this field is POD.

| TYPE    | Description                         |
|---------|-------------------------------------|
| 0b00000 | PE Reset, also see PE Reset Packet. |
| 0b00001 | Debug halt.                         |
| 0b00010 | Call.                               |
| 0b00011 | Trap.                               |
| 0b00100 | System Error.                       |
| 0b00110 | Inst debug.                         |
| 0b00111 | Data debug.                         |
| 0b01010 | Alignment.                          |
| 0b01011 | Inst Fault.                         |
| 0b01100 | Data Fault.                         |
| 0b01110 | IRQ.                                |
| 0b01111 | FIQ.                                |
| 0b10000 | IMPLEMENTATION DEFINED 0.           |
| 0b10001 | IMPLEMENTATION DEFINED 1.           |
| 0b10010 | IMPLEMENTATION DEFINED 2.           |

| TYPE    | Description                               |
|---------|-------------------------------------------|
| 0b10011 | IMPLEMENTATION DEFINED 3.                 |
| 0b10100 | IMPLEMENTATION DEFINED 4.                 |
| 0b10101 | IMPLEMENTATION DEFINED 5.                 |
| 0b10110 | IMPLEMENTATION DEFINED 6.                 |
| 0b10111 | IMPLEMENTATION DEFINED 7.                 |
| 0b11000 | Reserved. See Transaction Failure Packet. |

All other values are reserved. Reserved values might be defined in a future version of the architecture.

Virtual context identifier.

When this field is not output, the Virtual context identifier is the same as the most recently output Virtual context identifier.

If Virtual context identifier tracing is disabled, then one of the following must occur:

- This field is not traced.
- This field contains a value of zero.

The encoding for this field is POD.

See Virtual context identifier tracing.

## Additional information

For more information about the decoding of this packet see Parse\_ExceptionPacket().

For more information about the generation of this packet see Address compression.

For more information about the encoding of this packet see Instruction set encoding.

## VMID

## D5.3.28 Exception 32-bit Address IS1 Packet

## Purpose

Indicates that an exception has occurred.

Configurations

All.

Packet Layout

## Field descriptions

A

Preferred Exception Return address.

Preferred Exception Return address bit[0] always has the value 0b0.

The address is compressed relative to address history buffer entry 0.

The encoding for this field is Bit replacement.

Identifies the elements that are indicated by this packet.

The encoding for this field is POD.

| E    | Description                           |
|------|---------------------------------------|
| 0b01 | 1. Exception element (TYPE, ADDRESS). |
| 0b10 | 1. Target Address element (ADDRESS).  |
|      | 2. Exception element (TYPE, ADDRESS). |

All other values are reserved. Reserved values might be defined in a future version of the architecture.

The exception type.

The encoding for this field is POD.

E

TYPE

Figure D5-34 Exception 32-bit Address IS1 Packet

<!-- image -->

|      | 䕛ㅝ   | 䕛そ   |      |      |      |      |      |
|------|------|------|------|------|------|------|------|
| ⠰⤠   | 䅛㜺ㅝ  | 䅛㜺ㅝ  | 䅛㜺ㅝ  | 䅛㜺ㅝ  | 䅛㜺ㅝ  | 䅛㜺ㅝ  | 䅛㜺ㅝ  |
| 䅛ㄵ㨸  | 䅛ㄵ㨸  | 䅛ㄵ㨸  | 䅛ㄵ㨸  | 䅛ㄵ㨸  | 䅛ㄵ㨸  | 䅛ㄵ㨸  | 䅛ㄵ㨸  |
| 䅛㈳㨱㙝 | 䅛㈳㨱㙝 | 䅛㈳㨱㙝 | 䅛㈳㨱㙝 | 䅛㈳㨱㙝 | 䅛㈳㨱㙝 | 䅛㈳㨱㙝 | 䅛㈳㨱㙝 |
| 䅛㌱㨲㑝 | 䅛㌱㨲㑝 | 䅛㌱㨲㑝 | 䅛㌱㨲㑝 | 䅛㌱㨲㑝 | 䅛㌱㨲㑝 | 䅛㌱㨲㑝 | 䅛㌱㨲㑝 |

| TYPE    | Description                               |
|---------|-------------------------------------------|
| 0b00000 | PE Reset, also see PE Reset Packet.       |
| 0b00001 | Debug halt.                               |
| 0b00010 | Call.                                     |
| 0b00011 | Trap.                                     |
| 0b00100 | System Error.                             |
| 0b00110 | Inst debug.                               |
| 0b00111 | Data debug.                               |
| 0b01010 | Alignment.                                |
| 0b01011 | Inst Fault.                               |
| 0b01100 | Data Fault.                               |
| 0b01110 | IRQ.                                      |
| 0b01111 | FIQ.                                      |
| 0b10000 | IMPLEMENTATION DEFINED 0.                 |
| 0b10001 | IMPLEMENTATION DEFINED 1.                 |
| 0b10010 | IMPLEMENTATION DEFINED 2.                 |
| 0b10011 | IMPLEMENTATION DEFINED 3.                 |
| 0b10100 | IMPLEMENTATION DEFINED 4.                 |
| 0b10101 | IMPLEMENTATION DEFINED 5.                 |
| 0b10110 | IMPLEMENTATION DEFINED 6.                 |
| 0b10111 | IMPLEMENTATION DEFINED 7.                 |
| 0b11000 | Reserved. See Transaction Failure Packet. |

All other values are reserved. Reserved values might be defined in a future version of the architecture.

## Additional information

For more information about the decoding of this packet see Parse\_ExceptionPacket().

For more information about the generation of this packet see Address compression.

For more information about the encoding of this packet see Instruction set encoding.

## D5.3.29 Exception 32-bit Address IS1 with Context Packet

Purpose

Configurations

Indicates that an exception has occurred.

All.

Packet Layout - Variant 1

Packet Layout - Variant 2

Figure D5-35 Exception 32-bit Address IS1 with Context Packet (1)

<!-- image -->

Figure D5-36 Exception 32-bit Address IS1 with Context Packet (2)

<!-- image -->

## Packet Layout - Variant 3

## Packet Layout - Variant 4

## Field descriptions

A

Preferred Exception Return address.

Preferred Exception Return address bit[0] always has the value 0b0.

The address is compressed relative to address history buffer entry 0.

The encoding for this field is Bit replacement.

Figure D5-37 Exception 32-bit Address IS1 with Context Packet (3)

<!-- image -->

|       | 䕛ㅝ    |       |       | 呙偅    |       | 䕛そ    |       |
|-------|-------|-------|-------|-------|-------|-------|-------|
| ⠰⤠    | 䅛㜺ㅝ   | 䅛㜺ㅝ   | 䅛㜺ㅝ   | 䅛㜺ㅝ   | 䅛㜺ㅝ   | 䅛㜺ㅝ   | 䅛㜺ㅝ   |
| 䅛ㄵ㨸   | 䅛ㄵ㨸   | 䅛ㄵ㨸   | 䅛ㄵ㨸   | 䅛ㄵ㨸   | 䅛ㄵ㨸   | 䅛ㄵ㨸   | 䅛ㄵ㨸   |
| 䅛㈳㨱㙝  | 䅛㈳㨱㙝  | 䅛㈳㨱㙝  | 䅛㈳㨱㙝  | 䅛㈳㨱㙝  | 䅛㈳㨱㙝  | 䅛㈳㨱㙝  | 䅛㈳㨱㙝  |
| 䅛㌱㨲㑝  | 䅛㌱㨲㑝  | 䅛㌱㨲㑝  | 䅛㌱㨲㑝  | 䅛㌱㨲㑝  | 䅛㌱㨲㑝  | 䅛㌱㨲㑝  | 䅛㌱㨲㑝  |
|       |       | 乓     | 卆     | 乓     | ⠰⤠    | 䕌     |       |
| 噍䥄嬷㨰  | 噍䥄嬷㨰  | 噍䥄嬷㨰  | 噍䥄嬷㨰  | 噍䥄嬷㨰  | 噍䥄嬷㨰  | 噍䥄嬷㨰  | 噍䥄嬷㨰  |
| 噍䥄嬱㔺㡝 | 噍䥄嬱㔺㡝 | 噍䥄嬱㔺㡝 | 噍䥄嬱㔺㡝 | 噍䥄嬱㔺㡝 | 噍䥄嬱㔺㡝 | 噍䥄嬱㔺㡝 | 噍䥄嬱㔺㡝 |
| 噍䥄嬲㌺ㄶ | 噍䥄嬲㌺ㄶ | 噍䥄嬲㌺ㄶ | 噍䥄嬲㌺ㄶ | 噍䥄嬲㌺ㄶ | 噍䥄嬲㌺ㄶ | 噍䥄嬲㌺ㄶ | 噍䥄嬲㌺ㄶ |
| 噍䥄嬳ㄺ㈴ | 噍䥄嬳ㄺ㈴ | 噍䥄嬳ㄺ㈴ | 噍䥄嬳ㄺ㈴ | 噍䥄嬳ㄺ㈴ | 噍䥄嬳ㄺ㈴ | 噍䥄嬳ㄺ㈴ | 噍䥄嬳ㄺ㈴ |

Figure D5-38 Exception 32-bit Address IS1 with Context Packet (4)

<!-- image -->

|          | 䕛ㅝ       | 呙偅       | 呙偅       | 呙偅       | 呙偅       | 呙偅       |          |
|----------|----------|----------|----------|----------|----------|----------|----------|
| ⠰⤠       | 䅛㜺ㅝ      | 䅛㜺ㅝ      | 䅛㜺ㅝ      | 䅛㜺ㅝ      | 䅛㜺ㅝ      | 䅛㜺ㅝ      | 䅛㜺ㅝ      |
| 䅛ㄵ㨸      | 䅛ㄵ㨸      | 䅛ㄵ㨸      | 䅛ㄵ㨸      | 䅛ㄵ㨸      | 䅛ㄵ㨸      | 䅛ㄵ㨸      | 䅛ㄵ㨸      |
| 䅛㈳㨱㙝     | 䅛㈳㨱㙝     | 䅛㈳㨱㙝     | 䅛㈳㨱㙝     | 䅛㈳㨱㙝     | 䅛㈳㨱㙝     | 䅛㈳㨱㙝     | 䅛㈳㨱㙝     |
| 䅛㌱㨲㑝     | 䅛㌱㨲㑝     | 䅛㌱㨲㑝     | 䅛㌱㨲㑝     | 䅛㌱㨲㑝     | 䅛㌱㨲㑝     | 䅛㌱㨲㑝     | 䅛㌱㨲㑝     |
|          |          | 乓        | 卆        | 乓        | ⠰⤠       | 䕌        |          |
| 噍䥄嬷㨰     | 噍䥄嬷㨰     | 噍䥄嬷㨰     | 噍䥄嬷㨰     | 噍䥄嬷㨰     | 噍䥄嬷㨰     | 噍䥄嬷㨰     | 噍䥄嬷㨰     |
| 噍䥄嬱㔺㡝    | 噍䥄嬱㔺㡝    | 噍䥄嬱㔺㡝    | 噍䥄嬱㔺㡝    | 噍䥄嬱㔺㡝    | 噍䥄嬱㔺㡝    | 噍䥄嬱㔺㡝    | 噍䥄嬱㔺㡝    |
| 噍䥄嬲㌺ㄶ    | 噍䥄嬲㌺ㄶ    | 噍䥄嬲㌺ㄶ    | 噍䥄嬲㌺ㄶ    | 噍䥄嬲㌺ㄶ    | 噍䥄嬲㌺ㄶ    | 噍䥄嬲㌺ㄶ    | 噍䥄嬲㌺ㄶ    |
| 噍䥄嬳ㄺ㈴    | 噍䥄嬳ㄺ㈴    | 噍䥄嬳ㄺ㈴    | 噍䥄嬳ㄺ㈴    | 噍䥄嬳ㄺ㈴    | 噍䥄嬳ㄺ㈴    | 噍䥄嬳ㄺ㈴    | 噍䥄嬳ㄺ㈴    |
| 䍏乔䕘呉䑛㜺そ  | 䍏乔䕘呉䑛㜺そ  | 䍏乔䕘呉䑛㜺そ  | 䍏乔䕘呉䑛㜺そ  | 䍏乔䕘呉䑛㜺そ  | 䍏乔䕘呉䑛㜺そ  | 䍏乔䕘呉䑛㜺そ  | 䍏乔䕘呉䑛㜺そ  |
| 䍏乔䕘呉䑛ㄵ㨸  | 䍏乔䕘呉䑛ㄵ㨸  | 䍏乔䕘呉䑛ㄵ㨸  | 䍏乔䕘呉䑛ㄵ㨸  | 䍏乔䕘呉䑛ㄵ㨸  | 䍏乔䕘呉䑛ㄵ㨸  | 䍏乔䕘呉䑛ㄵ㨸  | 䍏乔䕘呉䑛ㄵ㨸  |
| 䍏乔䕘呉䑛㈳㨱㙝 | 䍏乔䕘呉䑛㈳㨱㙝 | 䍏乔䕘呉䑛㈳㨱㙝 | 䍏乔䕘呉䑛㈳㨱㙝 | 䍏乔䕘呉䑛㈳㨱㙝 | 䍏乔䕘呉䑛㈳㨱㙝 | 䍏乔䕘呉䑛㈳㨱㙝 | 䍏乔䕘呉䑛㈳㨱㙝 |
| 䍏乔䕘呉䑛㌱㨲㑝 | 䍏乔䕘呉䑛㌱㨲㑝 | 䍏乔䕘呉䑛㌱㨲㑝 | 䍏乔䕘呉䑛㌱㨲㑝 | 䍏乔䕘呉䑛㌱㨲㑝 | 䍏乔䕘呉䑛㌱㨲㑝 | 䍏乔䕘呉䑛㌱㨲㑝 | 䍏乔䕘呉䑛㌱㨲㑝 |

## CONTEXTID

E

EL

Context identifier.

When this field is not output, the Context identifier is the same as the most recently output Context identifier.

If Context identifier tracing is disabled, then one of the following must occur:

- This field is not traced.
- This field contains a value of zero.

The encoding for this field is POD.

See Context identifier tracing.

Identifies the elements that are indicated by this packet.

The encoding for this field is POD.

| E    | Description                                                                                     |
|------|-------------------------------------------------------------------------------------------------|
| 0b01 | 1. Context element . 2. Exception element (TYPE, ADDRESS).                                      |
| 0b10 | 1. Target Address element (ADDRESS). 2. Context element . 3. Exception element (TYPE, ADDRESS). |

All other values are reserved. Reserved values might be defined in a future version of the architecture.

Exception level at the Preferred Exception Return address.

The encoding for this field is POD.

| EL   | Description   |
|------|---------------|
| 0b00 | EL0.          |
| 0b01 | EL1.          |
| 0b10 | EL2.          |
| 0b11 | EL3.          |

NS

Security state.

The encoding for this field is POD.

With the NSE bit, indicates the Security state associated with the address.

| NSE   | NS   | Description                                                                                      |
|-------|------|--------------------------------------------------------------------------------------------------|
| 0b0   | 0b0  | Secure state. This value is defined only if Secure state is implemented, and reserved otherwise. |
| 0b0   | 0b1  | Non-secure state.                                                                                |
| 0b1   | 0b0  | Root state. This value is defined only if FEAT_RME is implemented, and reserved otherwise.       |
| 0b1   | 0b1  | Realm state. This value is defined only if FEAT_RME is implemented, and reserved otherwise.      |

NSE

Security state, for more information see the NS field.

The encoding for this field is POD.

SF

AArch64 state.

The encoding for this field is POD.

| SF   | Description                 |
|------|-----------------------------|
| 0b0  | The PE is in AArch32 state. |
| 0b1  | The PE is in AArch64 state. |

TYPE

The exception type.

The encoding for this field is POD.

| TYPE    | Description                         |
|---------|-------------------------------------|
| 0b00000 | PE Reset, also see PE Reset Packet. |
| 0b00001 | Debug halt.                         |
| 0b00010 | Call.                               |
| 0b00011 | Trap.                               |
| 0b00100 | System Error.                       |
| 0b00110 | Inst debug.                         |
| 0b00111 | Data debug.                         |
| 0b01010 | Alignment.                          |
| 0b01011 | Inst Fault.                         |
| 0b01100 | Data Fault.                         |
| 0b01110 | IRQ.                                |
| 0b01111 | FIQ.                                |
| 0b10000 | IMPLEMENTATION DEFINED 0.           |
| 0b10001 | IMPLEMENTATION DEFINED 1.           |
| 0b10010 | IMPLEMENTATION DEFINED 2.           |

| TYPE    | Description                               |
|---------|-------------------------------------------|
| 0b10011 | IMPLEMENTATION DEFINED 3.                 |
| 0b10100 | IMPLEMENTATION DEFINED 4.                 |
| 0b10101 | IMPLEMENTATION DEFINED 5.                 |
| 0b10110 | IMPLEMENTATION DEFINED 6.                 |
| 0b10111 | IMPLEMENTATION DEFINED 7.                 |
| 0b11000 | Reserved. See Transaction Failure Packet. |

All other values are reserved. Reserved values might be defined in a future version of the architecture.

Virtual context identifier.

When this field is not output, the Virtual context identifier is the same as the most recently output Virtual context identifier.

If Virtual context identifier tracing is disabled, then one of the following must occur:

- This field is not traced.
- This field contains a value of zero.

The encoding for this field is POD.

See Virtual context identifier tracing.

## Additional information

For more information about the decoding of this packet see Parse\_ExceptionPacket().

For more information about the generation of this packet see Address compression.

For more information about the encoding of this packet see Instruction set encoding.

## VMID

## D5.3.30 Exception 64-bit Address IS0 Packet

## Purpose

Configurations

E

TYPE

Indicates that an exception has occurred.

All.

Packet Layout

## Field descriptions

A

Preferred Exception Return address.

Preferred Exception Return address bits[1:0] always have the value 0b00.

The address is compressed relative to address history buffer entry 0.

The encoding for this field is Bit replacement.

Identifies the elements that are indicated by this packet.

The encoding for this field is POD.

| E    | Description                           |
|------|---------------------------------------|
| 0b01 | 1. Exception element (TYPE, ADDRESS). |
| 0b10 | 1. Target Address element (ADDRESS).  |

All other values are reserved. Reserved values might be defined in a future version of the architecture.

The exception type.

Figure D5-39 Exception 64-bit Address IS0 Packet

<!-- image -->

|      | 䕛ㅝ   | 呙偅   | 䕛そ   |      |      |      |      |
|------|------|------|------|------|------|------|------|
| ⠰⤠   | 䅛㠺㉝  | 䅛㠺㉝  | 䅛㠺㉝  | 䅛㠺㉝  | 䅛㠺㉝  | 䅛㠺㉝  | 䅛㠺㉝  |
| ⠰⤠   | 䅛ㄵ㨹  | 䅛ㄵ㨹  | 䅛ㄵ㨹  | 䅛ㄵ㨹  | 䅛ㄵ㨹  | 䅛ㄵ㨹  | 䅛ㄵ㨹  |
| 䅛㈳㨱㙝 | 䅛㈳㨱㙝 | 䅛㈳㨱㙝 | 䅛㈳㨱㙝 | 䅛㈳㨱㙝 | 䅛㈳㨱㙝 | 䅛㈳㨱㙝 | 䅛㈳㨱㙝 |
| 䅛㌱㨲㑝 | 䅛㌱㨲㑝 | 䅛㌱㨲㑝 | 䅛㌱㨲㑝 | 䅛㌱㨲㑝 | 䅛㌱㨲㑝 | 䅛㌱㨲㑝 | 䅛㌱㨲㑝 |
| 䅛㌹㨳㉝ | 䅛㌹㨳㉝ | 䅛㌹㨳㉝ | 䅛㌹㨳㉝ | 䅛㌹㨳㉝ | 䅛㌹㨳㉝ | 䅛㌹㨳㉝ | 䅛㌹㨳㉝ |
| 䅛㐷㨴そ | 䅛㐷㨴そ | 䅛㐷㨴そ | 䅛㐷㨴そ | 䅛㐷㨴そ | 䅛㐷㨴そ | 䅛㐷㨴そ | 䅛㐷㨴そ |
| 䅛㔵㨴㡝 | 䅛㔵㨴㡝 | 䅛㔵㨴㡝 | 䅛㔵㨴㡝 | 䅛㔵㨴㡝 | 䅛㔵㨴㡝 | 䅛㔵㨴㡝 | 䅛㔵㨴㡝 |
| 䅛㘳㨵㙝 | 䅛㘳㨵㙝 | 䅛㘳㨵㙝 | 䅛㘳㨵㙝 | 䅛㘳㨵㙝 | 䅛㘳㨵㙝 | 䅛㘳㨵㙝 | 䅛㘳㨵㙝 |

## The encoding for this field is POD.

| TYPE    | Description                               |
|---------|-------------------------------------------|
| 0b00000 | PE Reset, also see PE Reset Packet.       |
| 0b00001 | Debug halt.                               |
| 0b00010 | Call.                                     |
| 0b00011 | Trap.                                     |
| 0b00100 | System Error.                             |
| 0b00110 | Inst debug.                               |
| 0b00111 | Data debug.                               |
| 0b01010 | Alignment.                                |
| 0b01011 | Inst Fault.                               |
| 0b01100 | Data Fault.                               |
| 0b01110 | IRQ.                                      |
| 0b01111 | FIQ.                                      |
| 0b10000 | IMPLEMENTATION DEFINED 0.                 |
| 0b10001 | IMPLEMENTATION DEFINED 1.                 |
| 0b10010 | IMPLEMENTATION DEFINED 2.                 |
| 0b10011 | IMPLEMENTATION DEFINED 3.                 |
| 0b10100 | IMPLEMENTATION DEFINED 4.                 |
| 0b10101 | IMPLEMENTATION DEFINED 5.                 |
| 0b10110 | IMPLEMENTATION DEFINED 6.                 |
| 0b10111 | IMPLEMENTATION DEFINED 7.                 |
| 0b11000 | Reserved. See Transaction Failure Packet. |

All other values are reserved. Reserved values might be defined in a future version of the architecture.

## Additional information

For more information about the decoding of this packet see Parse\_ExceptionPacket().

For more information about the generation of this packet see Address compression.

For more information about the encoding of this packet see Instruction set encoding.

## D5.3.31 Exception 64-bit Address IS0 with Context Packet

Purpose

Configurations

Indicates that an exception has occurred.

All.

Packet Layout - Variant 1

Packet Layout - Variant 2

Figure D5-40 Exception 64-bit Address IS0 with Context Packet (1)

<!-- image -->

|      | 䕛ㅝ   |      |      | 呙偅   |      | 䕛そ   |      |
|------|------|------|------|------|------|------|------|
| ⠰⤠   | 䅛㠺㉝  | 䅛㠺㉝  | 䅛㠺㉝  | 䅛㠺㉝  | 䅛㠺㉝  | 䅛㠺㉝  | 䅛㠺㉝  |
| ⠰⤠   | 䅛ㄵ㨹  | 䅛ㄵ㨹  | 䅛ㄵ㨹  | 䅛ㄵ㨹  | 䅛ㄵ㨹  | 䅛ㄵ㨹  | 䅛ㄵ㨹  |
| 䅛㈳㨱㙝 | 䅛㈳㨱㙝 | 䅛㈳㨱㙝 | 䅛㈳㨱㙝 | 䅛㈳㨱㙝 | 䅛㈳㨱㙝 | 䅛㈳㨱㙝 | 䅛㈳㨱㙝 |
| 䅛㌱㨲㑝 | 䅛㌱㨲㑝 | 䅛㌱㨲㑝 | 䅛㌱㨲㑝 | 䅛㌱㨲㑝 | 䅛㌱㨲㑝 | 䅛㌱㨲㑝 | 䅛㌱㨲㑝 |
| 䅛㌹㨳㉝ | 䅛㌹㨳㉝ | 䅛㌹㨳㉝ | 䅛㌹㨳㉝ | 䅛㌹㨳㉝ | 䅛㌹㨳㉝ | 䅛㌹㨳㉝ | 䅛㌹㨳㉝ |
| 䅛㐷㨴そ | 䅛㐷㨴そ | 䅛㐷㨴そ | 䅛㐷㨴そ | 䅛㐷㨴そ | 䅛㐷㨴そ | 䅛㐷㨴そ | 䅛㐷㨴そ |
| 䅛㔵㨴㡝 | 䅛㔵㨴㡝 | 䅛㔵㨴㡝 | 䅛㔵㨴㡝 | 䅛㔵㨴㡝 | 䅛㔵㨴㡝 | 䅛㔵㨴㡝 | 䅛㔵㨴㡝 |
| 䅛㘳㨵㙝 | 䅛㘳㨵㙝 | 䅛㘳㨵㙝 | 䅛㘳㨵㙝 | 䅛㘳㨵㙝 | 䅛㘳㨵㙝 | 䅛㘳㨵㙝 | 䅛㘳㨵㙝 |
|      |      | 乓    | 卆    | 乓    | ⠰⤠   | 䕌    |      |

Figure D5-41 Exception 64-bit Address IS0 with Context Packet (2)

<!-- image -->

|          | 䕛ㅝ       |          |          | 呙偅       |          | 䕛そ       |          |
|----------|----------|----------|----------|----------|----------|----------|----------|
| ⠰⤠       | 䅛㠺㉝      | 䅛㠺㉝      | 䅛㠺㉝      | 䅛㠺㉝      | 䅛㠺㉝      | 䅛㠺㉝      | 䅛㠺㉝      |
| ⠰⤠       | 䅛ㄵ㨹      | 䅛ㄵ㨹      | 䅛ㄵ㨹      | 䅛ㄵ㨹      | 䅛ㄵ㨹      | 䅛ㄵ㨹      | 䅛ㄵ㨹      |
| 䅛㈳㨱㙝     | 䅛㈳㨱㙝     | 䅛㈳㨱㙝     | 䅛㈳㨱㙝     | 䅛㈳㨱㙝     | 䅛㈳㨱㙝     | 䅛㈳㨱㙝     | 䅛㈳㨱㙝     |
| 䅛㌱㨲㑝     | 䅛㌱㨲㑝     | 䅛㌱㨲㑝     | 䅛㌱㨲㑝     | 䅛㌱㨲㑝     | 䅛㌱㨲㑝     | 䅛㌱㨲㑝     | 䅛㌱㨲㑝     |
| 䅛㌹㨳㉝     | 䅛㌹㨳㉝     | 䅛㌹㨳㉝     | 䅛㌹㨳㉝     | 䅛㌹㨳㉝     | 䅛㌹㨳㉝     | 䅛㌹㨳㉝     | 䅛㌹㨳㉝     |
| 䅛㐷㨴そ     | 䅛㐷㨴そ     | 䅛㐷㨴そ     | 䅛㐷㨴そ     | 䅛㐷㨴そ     | 䅛㐷㨴そ     | 䅛㐷㨴そ     | 䅛㐷㨴そ     |
| 䅛㔵㨴㡝     | 䅛㔵㨴㡝     | 䅛㔵㨴㡝     | 䅛㔵㨴㡝     | 䅛㔵㨴㡝     | 䅛㔵㨴㡝     | 䅛㔵㨴㡝     | 䅛㔵㨴㡝     |
| 䅛㘳㨵㙝     | 䅛㘳㨵㙝     | 䅛㘳㨵㙝     | 䅛㘳㨵㙝     | 䅛㘳㨵㙝     | 䅛㘳㨵㙝     | 䅛㘳㨵㙝     | 䅛㘳㨵㙝     |
|          |          | 乓        | 卆        | 乓        | ⠰⤠       | 䕌        |          |
| 䍏乔䕘呉䑛㜺そ  | 䍏乔䕘呉䑛㜺そ  | 䍏乔䕘呉䑛㜺そ  | 䍏乔䕘呉䑛㜺そ  | 䍏乔䕘呉䑛㜺そ  | 䍏乔䕘呉䑛㜺そ  | 䍏乔䕘呉䑛㜺そ  | 䍏乔䕘呉䑛㜺そ  |
| 䍏乔䕘呉䑛ㄵ㨸  | 䍏乔䕘呉䑛ㄵ㨸  | 䍏乔䕘呉䑛ㄵ㨸  | 䍏乔䕘呉䑛ㄵ㨸  | 䍏乔䕘呉䑛ㄵ㨸  | 䍏乔䕘呉䑛ㄵ㨸  | 䍏乔䕘呉䑛ㄵ㨸  | 䍏乔䕘呉䑛ㄵ㨸  |
| 䍏乔䕘呉䑛㈳㨱㙝 | 䍏乔䕘呉䑛㈳㨱㙝 | 䍏乔䕘呉䑛㈳㨱㙝 | 䍏乔䕘呉䑛㈳㨱㙝 | 䍏乔䕘呉䑛㈳㨱㙝 | 䍏乔䕘呉䑛㈳㨱㙝 | 䍏乔䕘呉䑛㈳㨱㙝 | 䍏乔䕘呉䑛㈳㨱㙝 |
| 䍏乔䕘呉䑛㌱㨲㑝 | 䍏乔䕘呉䑛㌱㨲㑝 | 䍏乔䕘呉䑛㌱㨲㑝 | 䍏乔䕘呉䑛㌱㨲㑝 | 䍏乔䕘呉䑛㌱㨲㑝 | 䍏乔䕘呉䑛㌱㨲㑝 | 䍏乔䕘呉䑛㌱㨲㑝 | 䍏乔䕘呉䑛㌱㨲㑝 |

## Packet Layout - Variant 3

## Packet Layout - Variant 4

Figure D5-42 Exception 64-bit Address IS0 with Context Packet (3)

<!-- image -->

|       | 䕛ㅝ    |       |       | 呙偅    |       | 䕛そ    |       |
|-------|-------|-------|-------|-------|-------|-------|-------|
| ⠰⤠    | 䅛㠺㉝   | 䅛㠺㉝   | 䅛㠺㉝   | 䅛㠺㉝   | 䅛㠺㉝   | 䅛㠺㉝   | 䅛㠺㉝   |
| ⠰⤠    | 䅛ㄵ㨹   | 䅛ㄵ㨹   | 䅛ㄵ㨹   | 䅛ㄵ㨹   | 䅛ㄵ㨹   | 䅛ㄵ㨹   | 䅛ㄵ㨹   |
| 䅛㈳㨱㙝  | 䅛㈳㨱㙝  | 䅛㈳㨱㙝  | 䅛㈳㨱㙝  | 䅛㈳㨱㙝  | 䅛㈳㨱㙝  | 䅛㈳㨱㙝  | 䅛㈳㨱㙝  |
| 䅛㌱㨲㑝  | 䅛㌱㨲㑝  | 䅛㌱㨲㑝  | 䅛㌱㨲㑝  | 䅛㌱㨲㑝  | 䅛㌱㨲㑝  | 䅛㌱㨲㑝  | 䅛㌱㨲㑝  |
| 䅛㌹㨳㉝  | 䅛㌹㨳㉝  | 䅛㌹㨳㉝  | 䅛㌹㨳㉝  | 䅛㌹㨳㉝  | 䅛㌹㨳㉝  | 䅛㌹㨳㉝  | 䅛㌹㨳㉝  |
| 䅛㐷㨴そ  | 䅛㐷㨴そ  | 䅛㐷㨴そ  | 䅛㐷㨴そ  | 䅛㐷㨴そ  | 䅛㐷㨴そ  | 䅛㐷㨴そ  | 䅛㐷㨴そ  |
| 䅛㔵㨴㡝  | 䅛㔵㨴㡝  | 䅛㔵㨴㡝  | 䅛㔵㨴㡝  | 䅛㔵㨴㡝  | 䅛㔵㨴㡝  | 䅛㔵㨴㡝  | 䅛㔵㨴㡝  |
| 䅛㘳㨵㙝  | 䅛㘳㨵㙝  | 䅛㘳㨵㙝  | 䅛㘳㨵㙝  | 䅛㘳㨵㙝  | 䅛㘳㨵㙝  | 䅛㘳㨵㙝  | 䅛㘳㨵㙝  |
|       |       | 乓     | 卆     | 乓     | ⠰⤠    | 䕌     |       |
| 噍䥄嬷㨰  | 噍䥄嬷㨰  | 噍䥄嬷㨰  | 噍䥄嬷㨰  | 噍䥄嬷㨰  | 噍䥄嬷㨰  | 噍䥄嬷㨰  | 噍䥄嬷㨰  |
| 噍䥄嬱㔺㡝 | 噍䥄嬱㔺㡝 | 噍䥄嬱㔺㡝 | 噍䥄嬱㔺㡝 | 噍䥄嬱㔺㡝 | 噍䥄嬱㔺㡝 | 噍䥄嬱㔺㡝 | 噍䥄嬱㔺㡝 |
| 噍䥄嬲㌺ㄶ | 噍䥄嬲㌺ㄶ | 噍䥄嬲㌺ㄶ | 噍䥄嬲㌺ㄶ | 噍䥄嬲㌺ㄶ | 噍䥄嬲㌺ㄶ | 噍䥄嬲㌺ㄶ | 噍䥄嬲㌺ㄶ |
| 噍䥄嬳ㄺ㈴ | 噍䥄嬳ㄺ㈴ | 噍䥄嬳ㄺ㈴ | 噍䥄嬳ㄺ㈴ | 噍䥄嬳ㄺ㈴ | 噍䥄嬳ㄺ㈴ | 噍䥄嬳ㄺ㈴ | 噍䥄嬳ㄺ㈴ |

Figure D5-43 Exception 64-bit Address IS0 with Context Packet (4)

<!-- image -->

|          | 䕛ㅝ       |          |          | 呙偅       |          | 䕛そ       |          |
|----------|----------|----------|----------|----------|----------|----------|----------|
| ⠰⤠       | 䅛㠺㉝      | 䅛㠺㉝      | 䅛㠺㉝      | 䅛㠺㉝      | 䅛㠺㉝      | 䅛㠺㉝      | 䅛㠺㉝      |
| ⠰⤠       | 䅛ㄵ㨹      | 䅛ㄵ㨹      | 䅛ㄵ㨹      | 䅛ㄵ㨹      | 䅛ㄵ㨹      | 䅛ㄵ㨹      | 䅛ㄵ㨹      |
| 䅛㈳㨱㙝     | 䅛㈳㨱㙝     | 䅛㈳㨱㙝     | 䅛㈳㨱㙝     | 䅛㈳㨱㙝     | 䅛㈳㨱㙝     | 䅛㈳㨱㙝     | 䅛㈳㨱㙝     |
| 䅛㌱㨲㑝     | 䅛㌱㨲㑝     | 䅛㌱㨲㑝     | 䅛㌱㨲㑝     | 䅛㌱㨲㑝     | 䅛㌱㨲㑝     | 䅛㌱㨲㑝     | 䅛㌱㨲㑝     |
| 䅛㌹㨳㉝     | 䅛㌹㨳㉝     | 䅛㌹㨳㉝     | 䅛㌹㨳㉝     | 䅛㌹㨳㉝     | 䅛㌹㨳㉝     | 䅛㌹㨳㉝     | 䅛㌹㨳㉝     |
| 䅛㐷㨴そ     | 䅛㐷㨴そ     | 䅛㐷㨴そ     | 䅛㐷㨴そ     | 䅛㐷㨴そ     | 䅛㐷㨴そ     | 䅛㐷㨴そ     | 䅛㐷㨴そ     |
| 䅛㔵㨴㡝     | 䅛㔵㨴㡝     | 䅛㔵㨴㡝     | 䅛㔵㨴㡝     | 䅛㔵㨴㡝     | 䅛㔵㨴㡝     | 䅛㔵㨴㡝     | 䅛㔵㨴㡝     |
| 䅛㘳㨵㙝     | 䅛㘳㨵㙝     | 䅛㘳㨵㙝     | 䅛㘳㨵㙝     | 䅛㘳㨵㙝     | 䅛㘳㨵㙝     | 䅛㘳㨵㙝     | 䅛㘳㨵㙝     |
|          |          | 乓        | 卆        | 乓        | ⠰⤠       | 䕌        |          |
| 噍䥄嬷㨰     | 噍䥄嬷㨰     | 噍䥄嬷㨰     | 噍䥄嬷㨰     | 噍䥄嬷㨰     | 噍䥄嬷㨰     | 噍䥄嬷㨰     | 噍䥄嬷㨰     |
| 噍䥄嬱㔺㡝    | 噍䥄嬱㔺㡝    | 噍䥄嬱㔺㡝    | 噍䥄嬱㔺㡝    | 噍䥄嬱㔺㡝    | 噍䥄嬱㔺㡝    | 噍䥄嬱㔺㡝    | 噍䥄嬱㔺㡝    |
| 噍䥄嬲㌺ㄶ    | 噍䥄嬲㌺ㄶ    | 噍䥄嬲㌺ㄶ    | 噍䥄嬲㌺ㄶ    | 噍䥄嬲㌺ㄶ    | 噍䥄嬲㌺ㄶ    | 噍䥄嬲㌺ㄶ    | 噍䥄嬲㌺ㄶ    |
| 噍䥄嬳ㄺ㈴    | 噍䥄嬳ㄺ㈴    | 噍䥄嬳ㄺ㈴    | 噍䥄嬳ㄺ㈴    | 噍䥄嬳ㄺ㈴    | 噍䥄嬳ㄺ㈴    | 噍䥄嬳ㄺ㈴    | 噍䥄嬳ㄺ㈴    |
| 䍏乔䕘呉䑛㜺そ  | 䍏乔䕘呉䑛㜺そ  | 䍏乔䕘呉䑛㜺そ  | 䍏乔䕘呉䑛㜺そ  | 䍏乔䕘呉䑛㜺そ  | 䍏乔䕘呉䑛㜺そ  | 䍏乔䕘呉䑛㜺そ  | 䍏乔䕘呉䑛㜺そ  |
| 䍏乔䕘呉䑛ㄵ㨸  | 䍏乔䕘呉䑛ㄵ㨸  | 䍏乔䕘呉䑛ㄵ㨸  | 䍏乔䕘呉䑛ㄵ㨸  | 䍏乔䕘呉䑛ㄵ㨸  | 䍏乔䕘呉䑛ㄵ㨸  | 䍏乔䕘呉䑛ㄵ㨸  | 䍏乔䕘呉䑛ㄵ㨸  |
| 䍏乔䕘呉䑛㈳㨱㙝 | 䍏乔䕘呉䑛㈳㨱㙝 | 䍏乔䕘呉䑛㈳㨱㙝 | 䍏乔䕘呉䑛㈳㨱㙝 | 䍏乔䕘呉䑛㈳㨱㙝 | 䍏乔䕘呉䑛㈳㨱㙝 | 䍏乔䕘呉䑛㈳㨱㙝 | 䍏乔䕘呉䑛㈳㨱㙝 |
| 䍏乔䕘呉䑛㌱㨲㑝 | 䍏乔䕘呉䑛㌱㨲㑝 | 䍏乔䕘呉䑛㌱㨲㑝 | 䍏乔䕘呉䑛㌱㨲㑝 | 䍏乔䕘呉䑛㌱㨲㑝 | 䍏乔䕘呉䑛㌱㨲㑝 | 䍏乔䕘呉䑛㌱㨲㑝 | 䍏乔䕘呉䑛㌱㨲㑝 |

## Field descriptions

A

Preferred Exception Return address.

Preferred Exception Return address bits[1:0] always have the value 0b00.

The address is compressed relative to address history buffer entry 0.

The encoding for this field is Bit replacement.

Context identifier.

When this field is not output, the Context identifier is the same as the most recently output Context identifier.

If Context identifier tracing is disabled, then one of the following must occur:

- This field is not traced.
- This field contains a value of zero.

The encoding for this field is POD.

See Context identifier tracing.

Identifies the elements that are indicated by this packet.

The encoding for this field is POD.

| E    | Description                                                                                     |
|------|-------------------------------------------------------------------------------------------------|
| 0b01 | 1. Context element . 2. Exception element (TYPE, ADDRESS).                                      |
| 0b10 | 1. Target Address element (ADDRESS). 2. Context element . 3. Exception element (TYPE, ADDRESS). |

All other values are reserved. Reserved values might be defined in a future version of the architecture.

Exception level at the Preferred Exception Return address.

The encoding for this field is POD.

| EL   | Description   |
|------|---------------|
| 0b00 | EL0.          |
| 0b01 | EL1.          |
| 0b10 | EL2.          |
| 0b11 | EL3.          |

## CONTEXTID

E

EL

NS

Security state.

The encoding for this field is POD.

With the NSE bit, indicates the Security state associated with the address.

| NSE   | NS   | Description                                                                                      |
|-------|------|--------------------------------------------------------------------------------------------------|
| 0b0   | 0b0  | Secure state. This value is defined only if Secure state is implemented, and reserved otherwise. |
| 0b0   | 0b1  | Non-secure state.                                                                                |
| 0b1   | 0b0  | Root state. This value is defined only if FEAT_RME is implemented, and reserved otherwise.       |
| 0b1   | 0b1  | Realm state. This value is defined only if FEAT_RME is implemented, and reserved otherwise.      |

NSE

Security state, for more information see the NS field.

The encoding for this field is POD.

SF

AArch64 state.

The encoding for this field is POD.

| SF   | Description                 |
|------|-----------------------------|
| 0b0  | The PE is in AArch32 state. |
| 0b1  | The PE is in AArch64 state. |

## TYPE

The exception type.

The encoding for this field is POD.

| TYPE    | Description                         |
|---------|-------------------------------------|
| 0b00000 | PE Reset, also see PE Reset Packet. |
| 0b00001 | Debug halt.                         |
| 0b00010 | Call.                               |
| 0b00011 | Trap.                               |
| 0b00100 | System Error.                       |
| 0b00110 | Inst debug.                         |
| 0b00111 | Data debug.                         |
| 0b01010 | Alignment.                          |
| 0b01011 | Inst Fault.                         |

| TYPE    | Description                               |
|---------|-------------------------------------------|
| 0b01100 | Data Fault.                               |
| 0b01110 | IRQ.                                      |
| 0b01111 | FIQ.                                      |
| 0b10000 | IMPLEMENTATION DEFINED 0.                 |
| 0b10001 | IMPLEMENTATION DEFINED 1.                 |
| 0b10010 | IMPLEMENTATION DEFINED 2.                 |
| 0b10011 | IMPLEMENTATION DEFINED 3.                 |
| 0b10100 | IMPLEMENTATION DEFINED 4.                 |
| 0b10101 | IMPLEMENTATION DEFINED 5.                 |
| 0b10110 | IMPLEMENTATION DEFINED 6.                 |
| 0b10111 | IMPLEMENTATION DEFINED 7.                 |
| 0b11000 | Reserved. See Transaction Failure Packet. |

All other values are reserved. Reserved values might be defined in a future version of the architecture.

Virtual context identifier.

When this field is not output, the Virtual context identifier is the same as the most recently output Virtual context identifier.

If Virtual context identifier tracing is disabled, then one of the following must occur:

- This field is not traced.
- This field contains a value of zero.

The encoding for this field is POD.

See Virtual context identifier tracing.

## Additional information

For more information about the decoding of this packet see Parse\_ExceptionPacket().

For more information about the generation of this packet see Address compression.

For more information about the encoding of this packet see Instruction set encoding.

## VMID

## D5.3.32 Exception 64-bit Address IS1 Packet

## Purpose

Configurations

E

TYPE

Indicates that an exception has occurred.

All.

Packet Layout

## Field descriptions

A

Preferred Exception Return address.

Preferred Exception Return address bit[0] always has the value 0b0.

The address is compressed relative to address history buffer entry 0.

The encoding for this field is Bit replacement.

Identifies the elements that are indicated by this packet.

The encoding for this field is POD.

| E    | Description                           |
|------|---------------------------------------|
| 0b01 | 1. Exception element (TYPE, ADDRESS). |
| 0b10 | 1. Target Address element (ADDRESS).  |

All other values are reserved. Reserved values might be defined in a future version of the architecture.

The exception type.

Figure D5-44 Exception 64-bit Address IS1 Packet

<!-- image -->

|      | 䕛ㅝ   | 呙偅   | 䕛そ   |      |      |      |      |
|------|------|------|------|------|------|------|------|
| ⠰⤠   | 䅛㜺ㅝ  | 䅛㜺ㅝ  | 䅛㜺ㅝ  | 䅛㜺ㅝ  | 䅛㜺ㅝ  | 䅛㜺ㅝ  | 䅛㜺ㅝ  |
| 䅛ㄵ㨸  | 䅛ㄵ㨸  | 䅛ㄵ㨸  | 䅛ㄵ㨸  | 䅛ㄵ㨸  | 䅛ㄵ㨸  | 䅛ㄵ㨸  | 䅛ㄵ㨸  |
| 䅛㈳㨱㙝 | 䅛㈳㨱㙝 | 䅛㈳㨱㙝 | 䅛㈳㨱㙝 | 䅛㈳㨱㙝 | 䅛㈳㨱㙝 | 䅛㈳㨱㙝 | 䅛㈳㨱㙝 |
| 䅛㌱㨲㑝 | 䅛㌱㨲㑝 | 䅛㌱㨲㑝 | 䅛㌱㨲㑝 | 䅛㌱㨲㑝 | 䅛㌱㨲㑝 | 䅛㌱㨲㑝 | 䅛㌱㨲㑝 |
| 䅛㌹㨳㉝ | 䅛㌹㨳㉝ | 䅛㌹㨳㉝ | 䅛㌹㨳㉝ | 䅛㌹㨳㉝ | 䅛㌹㨳㉝ | 䅛㌹㨳㉝ | 䅛㌹㨳㉝ |
| 䅛㐷㨴そ | 䅛㐷㨴そ | 䅛㐷㨴そ | 䅛㐷㨴そ | 䅛㐷㨴そ | 䅛㐷㨴そ | 䅛㐷㨴そ | 䅛㐷㨴そ |
| 䅛㔵㨴㡝 | 䅛㔵㨴㡝 | 䅛㔵㨴㡝 | 䅛㔵㨴㡝 | 䅛㔵㨴㡝 | 䅛㔵㨴㡝 | 䅛㔵㨴㡝 | 䅛㔵㨴㡝 |
| 䅛㘳㨵㙝 | 䅛㘳㨵㙝 | 䅛㘳㨵㙝 | 䅛㘳㨵㙝 | 䅛㘳㨵㙝 | 䅛㘳㨵㙝 | 䅛㘳㨵㙝 | 䅛㘳㨵㙝 |

## The encoding for this field is POD.

| TYPE    | Description                               |
|---------|-------------------------------------------|
| 0b00000 | PE Reset, also see PE Reset Packet.       |
| 0b00001 | Debug halt.                               |
| 0b00010 | Call.                                     |
| 0b00011 | Trap.                                     |
| 0b00100 | System Error.                             |
| 0b00110 | Inst debug.                               |
| 0b00111 | Data debug.                               |
| 0b01010 | Alignment.                                |
| 0b01011 | Inst Fault.                               |
| 0b01100 | Data Fault.                               |
| 0b01110 | IRQ.                                      |
| 0b01111 | FIQ.                                      |
| 0b10000 | IMPLEMENTATION DEFINED 0.                 |
| 0b10001 | IMPLEMENTATION DEFINED 1.                 |
| 0b10010 | IMPLEMENTATION DEFINED 2.                 |
| 0b10011 | IMPLEMENTATION DEFINED 3.                 |
| 0b10100 | IMPLEMENTATION DEFINED 4.                 |
| 0b10101 | IMPLEMENTATION DEFINED 5.                 |
| 0b10110 | IMPLEMENTATION DEFINED 6.                 |
| 0b10111 | IMPLEMENTATION DEFINED 7.                 |
| 0b11000 | Reserved. See Transaction Failure Packet. |

All other values are reserved. Reserved values might be defined in a future version of the architecture.

## Additional information

For more information about the decoding of this packet see Parse\_ExceptionPacket().

For more information about the generation of this packet see Address compression.

For more information about the encoding of this packet see Instruction set encoding.

## D5.3.33 Exception 64-bit Address IS1 with Context Packet

Purpose

Configurations

Indicates that an exception has occurred.

All.

Packet Layout - Variant 1

Packet Layout - Variant 2

<!-- image -->

|      | 䕛ㅝ   |      |      | 呙偅   |      | 䕛そ   |      |
|------|------|------|------|------|------|------|------|
| ⠰⤠   | 䅛㜺ㅝ  | 䅛㜺ㅝ  | 䅛㜺ㅝ  | 䅛㜺ㅝ  | 䅛㜺ㅝ  | 䅛㜺ㅝ  | 䅛㜺ㅝ  |
| 䅛ㄵ㨸  | 䅛ㄵ㨸  | 䅛ㄵ㨸  | 䅛ㄵ㨸  | 䅛ㄵ㨸  | 䅛ㄵ㨸  | 䅛ㄵ㨸  | 䅛ㄵ㨸  |
| 䅛㈳㨱㙝 | 䅛㈳㨱㙝 | 䅛㈳㨱㙝 | 䅛㈳㨱㙝 | 䅛㈳㨱㙝 | 䅛㈳㨱㙝 | 䅛㈳㨱㙝 | 䅛㈳㨱㙝 |
| 䅛㌱㨲㑝 | 䅛㌱㨲㑝 | 䅛㌱㨲㑝 | 䅛㌱㨲㑝 | 䅛㌱㨲㑝 | 䅛㌱㨲㑝 | 䅛㌱㨲㑝 | 䅛㌱㨲㑝 |
| 䅛㌹㨳㉝ | 䅛㌹㨳㉝ | 䅛㌹㨳㉝ | 䅛㌹㨳㉝ | 䅛㌹㨳㉝ | 䅛㌹㨳㉝ | 䅛㌹㨳㉝ | 䅛㌹㨳㉝ |
| 䅛㐷㨴そ | 䅛㐷㨴そ | 䅛㐷㨴そ | 䅛㐷㨴そ | 䅛㐷㨴そ | 䅛㐷㨴そ | 䅛㐷㨴そ | 䅛㐷㨴そ |
| 䅛㔵㨴㡝 | 䅛㔵㨴㡝 | 䅛㔵㨴㡝 | 䅛㔵㨴㡝 | 䅛㔵㨴㡝 | 䅛㔵㨴㡝 | 䅛㔵㨴㡝 | 䅛㔵㨴㡝 |
| 䅛㘳㨵㙝 | 䅛㘳㨵㙝 | 䅛㘳㨵㙝 | 䅛㘳㨵㙝 | 䅛㘳㨵㙝 | 䅛㘳㨵㙝 | 䅛㘳㨵㙝 | 䅛㘳㨵㙝 |
|      |      | 乓    | 卆    | 乓    | ⠰⤠   | 䕌    |      |

Figure D5-45 Exception 64-bit Address IS1 with Context Packet (1)

<!-- image -->

|          | 䕛ㅝ       |          |          | 呙偅       |          | 䕛そ       |          |
|----------|----------|----------|----------|----------|----------|----------|----------|
| ⠰⤠       | 䅛㜺ㅝ      | 䅛㜺ㅝ      | 䅛㜺ㅝ      | 䅛㜺ㅝ      | 䅛㜺ㅝ      | 䅛㜺ㅝ      | 䅛㜺ㅝ      |
| 䅛ㄵ㨸      | 䅛ㄵ㨸      | 䅛ㄵ㨸      | 䅛ㄵ㨸      | 䅛ㄵ㨸      | 䅛ㄵ㨸      | 䅛ㄵ㨸      | 䅛ㄵ㨸      |
| 䅛㈳㨱㙝     | 䅛㈳㨱㙝     | 䅛㈳㨱㙝     | 䅛㈳㨱㙝     | 䅛㈳㨱㙝     | 䅛㈳㨱㙝     | 䅛㈳㨱㙝     | 䅛㈳㨱㙝     |
| 䅛㌱㨲㑝     | 䅛㌱㨲㑝     | 䅛㌱㨲㑝     | 䅛㌱㨲㑝     | 䅛㌱㨲㑝     | 䅛㌱㨲㑝     | 䅛㌱㨲㑝     | 䅛㌱㨲㑝     |
| 䅛㌹㨳㉝     | 䅛㌹㨳㉝     | 䅛㌹㨳㉝     | 䅛㌹㨳㉝     | 䅛㌹㨳㉝     | 䅛㌹㨳㉝     | 䅛㌹㨳㉝     | 䅛㌹㨳㉝     |
| 䅛㐷㨴そ     | 䅛㐷㨴そ     | 䅛㐷㨴そ     | 䅛㐷㨴そ     | 䅛㐷㨴そ     | 䅛㐷㨴そ     | 䅛㐷㨴そ     | 䅛㐷㨴そ     |
| 䅛㔵㨴㡝     | 䅛㔵㨴㡝     | 䅛㔵㨴㡝     | 䅛㔵㨴㡝     | 䅛㔵㨴㡝     | 䅛㔵㨴㡝     | 䅛㔵㨴㡝     | 䅛㔵㨴㡝     |
| 䅛㘳㨵㙝     | 䅛㘳㨵㙝     | 䅛㘳㨵㙝     | 䅛㘳㨵㙝     | 䅛㘳㨵㙝     | 䅛㘳㨵㙝     | 䅛㘳㨵㙝     | 䅛㘳㨵㙝     |
|          |          | 乓        | 卆        | 乓        | ⠰⤠       | 䕌        |          |
| 䍏乔䕘呉䑛㜺そ  | 䍏乔䕘呉䑛㜺そ  | 䍏乔䕘呉䑛㜺そ  | 䍏乔䕘呉䑛㜺そ  | 䍏乔䕘呉䑛㜺そ  | 䍏乔䕘呉䑛㜺そ  | 䍏乔䕘呉䑛㜺そ  | 䍏乔䕘呉䑛㜺そ  |
| 䍏乔䕘呉䑛ㄵ㨸  | 䍏乔䕘呉䑛ㄵ㨸  | 䍏乔䕘呉䑛ㄵ㨸  | 䍏乔䕘呉䑛ㄵ㨸  | 䍏乔䕘呉䑛ㄵ㨸  | 䍏乔䕘呉䑛ㄵ㨸  | 䍏乔䕘呉䑛ㄵ㨸  | 䍏乔䕘呉䑛ㄵ㨸  |
| 䍏乔䕘呉䑛㈳㨱㙝 | 䍏乔䕘呉䑛㈳㨱㙝 | 䍏乔䕘呉䑛㈳㨱㙝 | 䍏乔䕘呉䑛㈳㨱㙝 | 䍏乔䕘呉䑛㈳㨱㙝 | 䍏乔䕘呉䑛㈳㨱㙝 | 䍏乔䕘呉䑛㈳㨱㙝 | 䍏乔䕘呉䑛㈳㨱㙝 |
| 䍏乔䕘呉䑛㌱㨲㑝 | 䍏乔䕘呉䑛㌱㨲㑝 | 䍏乔䕘呉䑛㌱㨲㑝 | 䍏乔䕘呉䑛㌱㨲㑝 | 䍏乔䕘呉䑛㌱㨲㑝 | 䍏乔䕘呉䑛㌱㨲㑝 | 䍏乔䕘呉䑛㌱㨲㑝 | 䍏乔䕘呉䑛㌱㨲㑝 |

Figure D5-46 Exception 64-bit Address IS1 with Context Packet (2)

## Packet Layout - Variant 3

## Packet Layout - Variant 4

Figure D5-47 Exception 64-bit Address IS1 with Context Packet (3)

<!-- image -->

|       | 䕛ㅝ    |       |       | 呙偅    |       | 䕛そ    |       |
|-------|-------|-------|-------|-------|-------|-------|-------|
| ⠰⤠    |       |       |       | 䅛㜺ㅝ   |       |       |       |
| 䅛ㄵ㨸   | 䅛ㄵ㨸   | 䅛ㄵ㨸   | 䅛ㄵ㨸   | 䅛ㄵ㨸   |       |       |       |
| 䅛㈳㨱㙝  | 䅛㈳㨱㙝  | 䅛㈳㨱㙝  | 䅛㈳㨱㙝  | 䅛㈳㨱㙝  |       |       |       |
| 䅛㌱㨲㑝  | 䅛㌱㨲㑝  | 䅛㌱㨲㑝  | 䅛㌱㨲㑝  | 䅛㌱㨲㑝  |       |       |       |
| 䅛㌹㨳㉝  | 䅛㌹㨳㉝  | 䅛㌹㨳㉝  | 䅛㌹㨳㉝  | 䅛㌹㨳㉝  |       |       |       |
| 䅛㐷㨴そ  | 䅛㐷㨴そ  | 䅛㐷㨴そ  | 䅛㐷㨴そ  | 䅛㐷㨴そ  |       |       |       |
| 䅛㔵㨴㡝  | 䅛㔵㨴㡝  | 䅛㔵㨴㡝  | 䅛㔵㨴㡝  | 䅛㔵㨴㡝  |       |       |       |
| 䅛㘳㨵㙝  | 䅛㘳㨵㙝  | 䅛㘳㨵㙝  | 䅛㘳㨵㙝  | 䅛㘳㨵㙝  | 䅛㘳㨵㙝  | 䅛㘳㨵㙝  | 䅛㘳㨵㙝  |
|       |       | 乓     | 卆     | 乓     | ⠰⤠    | 䕌     |       |
| 噍䥄嬷㨰  | 噍䥄嬷㨰  | 噍䥄嬷㨰  | 噍䥄嬷㨰  | 噍䥄嬷㨰  | 噍䥄嬷㨰  | 噍䥄嬷㨰  | 噍䥄嬷㨰  |
| 噍䥄嬱㔺㡝 | 噍䥄嬱㔺㡝 | 噍䥄嬱㔺㡝 | 噍䥄嬱㔺㡝 | 噍䥄嬱㔺㡝 | 噍䥄嬱㔺㡝 | 噍䥄嬱㔺㡝 | 噍䥄嬱㔺㡝 |
| 噍䥄嬲㌺ㄶ | 噍䥄嬲㌺ㄶ | 噍䥄嬲㌺ㄶ | 噍䥄嬲㌺ㄶ | 噍䥄嬲㌺ㄶ | 噍䥄嬲㌺ㄶ | 噍䥄嬲㌺ㄶ | 噍䥄嬲㌺ㄶ |
| 噍䥄嬳ㄺ㈴ | 噍䥄嬳ㄺ㈴ | 噍䥄嬳ㄺ㈴ | 噍䥄嬳ㄺ㈴ | 噍䥄嬳ㄺ㈴ | 噍䥄嬳ㄺ㈴ | 噍䥄嬳ㄺ㈴ | 噍䥄嬳ㄺ㈴ |

Figure D5-48 Exception 64-bit Address IS1 with Context Packet (4)

<!-- image -->

|          | 䕛ㅝ       |          |          | 呙偅       |          | 䕛そ       |          |
|----------|----------|----------|----------|----------|----------|----------|----------|
| ⠰⤠       |          |          |          | 䅛㜺ㅝ      |          |          |          |
|          |          |          | 䅛ㄵ㨸      | 䅛ㄵ㨸      |          |          |          |
|          |          |          | 䅛㈳㨱㙝     | 䅛㈳㨱㙝     |          |          |          |
|          |          |          | 䅛㌱㨲㑝     | 䅛㌱㨲㑝     |          |          |          |
|          |          |          | 䅛㌹㨳㉝     | 䅛㌹㨳㉝     |          |          |          |
|          |          |          | 䅛㐷㨴そ     | 䅛㐷㨴そ     |          |          |          |
|          |          |          | 䅛㔵㨴㡝     | 䅛㔵㨴㡝     |          |          |          |
| 䅛㘳㨵㙝     | 䅛㘳㨵㙝     | 䅛㘳㨵㙝     | 䅛㘳㨵㙝     | 䅛㘳㨵㙝     | 䅛㘳㨵㙝     | 䅛㘳㨵㙝     | 䅛㘳㨵㙝     |
|          |          | 乓        | 卆        | 乓        | ⠰⤠       | 䕌        |          |
| 噍䥄嬷㨰     | 噍䥄嬷㨰     | 噍䥄嬷㨰     | 噍䥄嬷㨰     | 噍䥄嬷㨰     | 噍䥄嬷㨰     | 噍䥄嬷㨰     | 噍䥄嬷㨰     |
| 噍䥄嬱㔺㡝    | 噍䥄嬱㔺㡝    | 噍䥄嬱㔺㡝    | 噍䥄嬱㔺㡝    | 噍䥄嬱㔺㡝    | 噍䥄嬱㔺㡝    | 噍䥄嬱㔺㡝    | 噍䥄嬱㔺㡝    |
| 噍䥄嬲㌺ㄶ    | 噍䥄嬲㌺ㄶ    | 噍䥄嬲㌺ㄶ    | 噍䥄嬲㌺ㄶ    | 噍䥄嬲㌺ㄶ    | 噍䥄嬲㌺ㄶ    | 噍䥄嬲㌺ㄶ    | 噍䥄嬲㌺ㄶ    |
| 噍䥄嬳ㄺ㈴    | 噍䥄嬳ㄺ㈴    | 噍䥄嬳ㄺ㈴    | 噍䥄嬳ㄺ㈴    | 噍䥄嬳ㄺ㈴    | 噍䥄嬳ㄺ㈴    | 噍䥄嬳ㄺ㈴    | 噍䥄嬳ㄺ㈴    |
| 䍏乔䕘呉䑛㜺そ  | 䍏乔䕘呉䑛㜺そ  | 䍏乔䕘呉䑛㜺そ  | 䍏乔䕘呉䑛㜺そ  | 䍏乔䕘呉䑛㜺そ  | 䍏乔䕘呉䑛㜺そ  | 䍏乔䕘呉䑛㜺そ  | 䍏乔䕘呉䑛㜺そ  |
| 䍏乔䕘呉䑛ㄵ㨸  | 䍏乔䕘呉䑛ㄵ㨸  | 䍏乔䕘呉䑛ㄵ㨸  | 䍏乔䕘呉䑛ㄵ㨸  | 䍏乔䕘呉䑛ㄵ㨸  | 䍏乔䕘呉䑛ㄵ㨸  | 䍏乔䕘呉䑛ㄵ㨸  | 䍏乔䕘呉䑛ㄵ㨸  |
| 䍏乔䕘呉䑛㈳㨱㙝 | 䍏乔䕘呉䑛㈳㨱㙝 | 䍏乔䕘呉䑛㈳㨱㙝 | 䍏乔䕘呉䑛㈳㨱㙝 | 䍏乔䕘呉䑛㈳㨱㙝 | 䍏乔䕘呉䑛㈳㨱㙝 | 䍏乔䕘呉䑛㈳㨱㙝 | 䍏乔䕘呉䑛㈳㨱㙝 |
| 䍏乔䕘呉䑛㌱㨲㑝 | 䍏乔䕘呉䑛㌱㨲㑝 | 䍏乔䕘呉䑛㌱㨲㑝 | 䍏乔䕘呉䑛㌱㨲㑝 | 䍏乔䕘呉䑛㌱㨲㑝 | 䍏乔䕘呉䑛㌱㨲㑝 | 䍏乔䕘呉䑛㌱㨲㑝 | 䍏乔䕘呉䑛㌱㨲㑝 |

## Field descriptions

A

Preferred Exception Return address.

Preferred Exception Return address bit[0] always has the value 0b0.

The address is compressed relative to address history buffer entry 0.

The encoding for this field is Bit replacement.

Context identifier.

When this field is not output, the Context identifier is the same as the most recently output Context identifier.

If Context identifier tracing is disabled, then one of the following must occur:

- This field is not traced.
- This field contains a value of zero.

The encoding for this field is POD.

See Context identifier tracing.

Identifies the elements that are indicated by this packet.

The encoding for this field is POD.

| E    | Description                                                                                     |
|------|-------------------------------------------------------------------------------------------------|
| 0b01 | 1. Context element . 2. Exception element (TYPE, ADDRESS).                                      |
| 0b10 | 1. Target Address element (ADDRESS). 2. Context element . 3. Exception element (TYPE, ADDRESS). |

All other values are reserved. Reserved values might be defined in a future version of the architecture.

Exception level at the Preferred Exception Return address.

The encoding for this field is POD.

| EL   | Description   |
|------|---------------|
| 0b00 | EL0.          |
| 0b01 | EL1.          |
| 0b10 | EL2.          |
| 0b11 | EL3.          |

## CONTEXTID

E

EL

NS

Security state.

The encoding for this field is POD.

With the NSE bit, indicates the Security state associated with the address.

| NSE   | NS   | Description                                                                                      |
|-------|------|--------------------------------------------------------------------------------------------------|
| 0b0   | 0b0  | Secure state. This value is defined only if Secure state is implemented, and reserved otherwise. |
| 0b0   | 0b1  | Non-secure state.                                                                                |
| 0b1   | 0b0  | Root state. This value is defined only if FEAT_RME is implemented, and reserved otherwise.       |
| 0b1   | 0b1  | Realm state. This value is defined only if FEAT_RME is implemented, and reserved otherwise.      |

NSE

Security state, for more information see the NS field.

The encoding for this field is POD.

SF

AArch64 state.

The encoding for this field is POD.

| SF   | Description                 |
|------|-----------------------------|
| 0b0  | The PE is in AArch32 state. |
| 0b1  | The PE is in AArch64 state. |

## TYPE

The exception type.

The encoding for this field is POD.

| TYPE    | Description                         |
|---------|-------------------------------------|
| 0b00000 | PE Reset, also see PE Reset Packet. |
| 0b00001 | Debug halt.                         |
| 0b00010 | Call.                               |
| 0b00011 | Trap.                               |
| 0b00100 | System Error.                       |
| 0b00110 | Inst debug.                         |
| 0b00111 | Data debug.                         |
| 0b01010 | Alignment.                          |
| 0b01011 | Inst Fault.                         |

| TYPE    | Description                               |
|---------|-------------------------------------------|
| 0b01100 | Data Fault.                               |
| 0b01110 | IRQ.                                      |
| 0b01111 | FIQ.                                      |
| 0b10000 | IMPLEMENTATION DEFINED 0.                 |
| 0b10001 | IMPLEMENTATION DEFINED 1.                 |
| 0b10010 | IMPLEMENTATION DEFINED 2.                 |
| 0b10011 | IMPLEMENTATION DEFINED 3.                 |
| 0b10100 | IMPLEMENTATION DEFINED 4.                 |
| 0b10101 | IMPLEMENTATION DEFINED 5.                 |
| 0b10110 | IMPLEMENTATION DEFINED 6.                 |
| 0b10111 | IMPLEMENTATION DEFINED 7.                 |
| 0b11000 | Reserved. See Transaction Failure Packet. |

All other values are reserved. Reserved values might be defined in a future version of the architecture.

Virtual context identifier.

When this field is not output, the Virtual context identifier is the same as the most recently output Virtual context identifier.

If Virtual context identifier tracing is disabled, then one of the following must occur:

- This field is not traced.
- This field contains a value of zero.

The encoding for this field is POD.

See Virtual context identifier tracing.

## Additional information

For more information about the decoding of this packet see Parse\_ExceptionPacket().

For more information about the generation of this packet see Address compression.

For more information about the encoding of this packet see Instruction set encoding.

## VMID

## D5.3.34 Exception Exact Match Address Packet

Purpose

Indicates that an exception has occurred.

Configurations

All.

Packet Layout

## Field descriptions

A

Preferred Exception Return address.

The encoding for this field is POD.

| A    | Description                                                                   |
|------|-------------------------------------------------------------------------------|
| 0b00 | The Preferred Exception Return is the same as address history buffer entry 0. |
| 0b01 | The Preferred Exception Return is the same as address history buffer entry 1. |
| 0b10 | The Preferred Exception Return is the same as address history buffer entry 2. |

E

TYPE

Figure D5-49 Exception Exact Match Address Packet

<!-- image -->

Identifies the elements that are indicated by this packet.

The encoding for this field is POD.

| E    | Description                           |
|------|---------------------------------------|
| 0b01 | 1. Exception element (TYPE, ADDRESS). |
| 0b10 | 1. Target Address element (ADDRESS).  |
|      | 2. Exception element (TYPE, ADDRESS). |

All other values are reserved. Reserved values might be defined in a future version of the architecture.

The exception type.

The encoding for this field is POD.

| TYPE    | Description                               |
|---------|-------------------------------------------|
| 0b00000 | PE Reset, also see PE Reset Packet.       |
| 0b00001 | Debug halt.                               |
| 0b00010 | Call.                                     |
| 0b00011 | Trap.                                     |
| 0b00100 | System Error.                             |
| 0b00110 | Inst debug.                               |
| 0b00111 | Data debug.                               |
| 0b01010 | Alignment.                                |
| 0b01011 | Inst Fault.                               |
| 0b01100 | Data Fault.                               |
| 0b01110 | IRQ.                                      |
| 0b01111 | FIQ.                                      |
| 0b10000 | IMPLEMENTATION DEFINED 0.                 |
| 0b10001 | IMPLEMENTATION DEFINED 1.                 |
| 0b10010 | IMPLEMENTATION DEFINED 2.                 |
| 0b10011 | IMPLEMENTATION DEFINED 3.                 |
| 0b10100 | IMPLEMENTATION DEFINED 4.                 |
| 0b10101 | IMPLEMENTATION DEFINED 5.                 |
| 0b10110 | IMPLEMENTATION DEFINED 6.                 |
| 0b10111 | IMPLEMENTATION DEFINED 7.                 |
| 0b11000 | Reserved. See Transaction Failure Packet. |

All other values are reserved. Reserved values might be defined in a future version of the architecture.

## Additional information

For more information about the decoding of this packet see Parse\_ExceptionPacket().

For more information about the generation of this packet see Address compression.

## D5.3.35 Exception Short Address IS0 Packet

## Purpose

Configurations

C0

Indicates that an exception has occurred.

All.

Packet Layout

## Field descriptions

A

Preferred Exception Return address.

Preferred Exception Return address bits[1:0] always have the value 0b00.

The address is compressed relative to address history buffer entry 0.

The encoding for this field is Bit replacement.

Continuation Bit.

The encoding for this field is Unary code.

| C0   | Description                                     |
|------|-------------------------------------------------|
| 0b0  | Last byte in this section.                      |
| 0b1  | At least one more byte follows in this section. |

E

Figure D5-50 Exception Short Address IS0 Packet

<!-- image -->

Identifies the elements that are indicated by this packet.

The encoding for this field is POD.

| E    | Description                           |
|------|---------------------------------------|
| 0b01 | 1. Exception element (TYPE, ADDRESS). |

| E    | Description                          |
|------|--------------------------------------|
| 0b10 | 1. Target Address element (ADDRESS). |

All other values are reserved. Reserved values might be defined in a future version of the architecture.

The exception type.

The encoding for this field is POD.

| TYPE    | Description                               |
|---------|-------------------------------------------|
| 0b00000 | PE Reset, also see PE Reset Packet.       |
| 0b00001 | Debug halt.                               |
| 0b00010 | Call.                                     |
| 0b00011 | Trap.                                     |
| 0b00100 | System Error.                             |
| 0b00110 | Inst debug.                               |
| 0b00111 | Data debug.                               |
| 0b01010 | Alignment.                                |
| 0b01011 | Inst Fault.                               |
| 0b01100 | Data Fault.                               |
| 0b01110 | IRQ.                                      |
| 0b01111 | FIQ.                                      |
| 0b10000 | IMPLEMENTATION DEFINED 0.                 |
| 0b10001 | IMPLEMENTATION DEFINED 1.                 |
| 0b10010 | IMPLEMENTATION DEFINED 2.                 |
| 0b10011 | IMPLEMENTATION DEFINED 3.                 |
| 0b10100 | IMPLEMENTATION DEFINED 4.                 |
| 0b10101 | IMPLEMENTATION DEFINED 5.                 |
| 0b10110 | IMPLEMENTATION DEFINED 6.                 |
| 0b10111 | IMPLEMENTATION DEFINED 7.                 |
| 0b11000 | Reserved. See Transaction Failure Packet. |

All other values are reserved. Reserved values might be defined in a future version of the architecture.

## Additional information

For more information about the decoding of this packet see Parse\_ExceptionPacket().

For more information about the generation of this packet see Address compression.

For more information about the encoding of this packet see Instruction set encoding.

## TYPE

## D5.3.36 Exception Short Address IS1 Packet

## Purpose

Indicates that an exception has occurred.

Configurations

All.

Packet Layout

## Field descriptions

A

Preferred Exception Return address.

Preferred Exception Return address bit[0] always has the value 0b0.

The address is compressed relative to address history buffer entry 0.

The encoding for this field is Bit replacement.

Continuation Bit.

The encoding for this field is Unary code.

| C0   | Description                                     |
|------|-------------------------------------------------|
| 0b0  | Last byte in this section.                      |
| 0b1  | At least one more byte follows in this section. |

E

C0

Figure D5-51 Exception Short Address IS1 Packet

<!-- image -->

Identifies the elements that are indicated by this packet.

The encoding for this field is POD.

| E    | Description                           |
|------|---------------------------------------|
| 0b01 | 1. Exception element (TYPE, ADDRESS). |

| E    | Description                          |
|------|--------------------------------------|
| 0b10 | 1. Target Address element (ADDRESS). |

All other values are reserved. Reserved values might be defined in a future version of the architecture.

The exception type.

The encoding for this field is POD.

| TYPE    | Description                               |
|---------|-------------------------------------------|
| 0b00000 | PE Reset, also see PE Reset Packet.       |
| 0b00001 | Debug halt.                               |
| 0b00010 | Call.                                     |
| 0b00011 | Trap.                                     |
| 0b00100 | System Error.                             |
| 0b00110 | Inst debug.                               |
| 0b00111 | Data debug.                               |
| 0b01010 | Alignment.                                |
| 0b01011 | Inst Fault.                               |
| 0b01100 | Data Fault.                               |
| 0b01110 | IRQ.                                      |
| 0b01111 | FIQ.                                      |
| 0b10000 | IMPLEMENTATION DEFINED 0.                 |
| 0b10001 | IMPLEMENTATION DEFINED 1.                 |
| 0b10010 | IMPLEMENTATION DEFINED 2.                 |
| 0b10011 | IMPLEMENTATION DEFINED 3.                 |
| 0b10100 | IMPLEMENTATION DEFINED 4.                 |
| 0b10101 | IMPLEMENTATION DEFINED 5.                 |
| 0b10110 | IMPLEMENTATION DEFINED 6.                 |
| 0b10111 | IMPLEMENTATION DEFINED 7.                 |
| 0b11000 | Reserved. See Transaction Failure Packet. |

All other values are reserved. Reserved values might be defined in a future version of the architecture.

## Additional information

For more information about the decoding of this packet see Parse\_ExceptionPacket().

For more information about the generation of this packet see Address compression.

For more information about the encoding of this packet see Instruction set encoding.

## TYPE

## D5.3.37 Ignore Packet

Purpose

Configurations

Packet Layout

To align packet boundary to memory boundary.

All.

Figure D5-52 Ignore Packet

<!-- image -->

## D5.3.38 Instrumentation Packet

## Purpose

Indicates an Instrumentation element.

## Configurations

When FEAT\_ITE is implemented.

## Packet Layout

## Field descriptions

EL

Exception level at which the corresponding TRCIT instruction was executed.

The encoding for this field is POD.

| EL   | Description   |
|------|---------------|
| 0b00 | EL0           |
| 0b01 | EL1           |
| 0b10 | EL2           |
| 0b11 | EL3           |

## VALUE

Value provided in Xn of the TRCIT instruction.

The encoding for this field is POD.

## Element sequence

This packet encodes the following sequence:

1. Instrumentation element.

Figure D5-53 Instrumentation Packet

| 7                          | 6                          | 5                          | 4                          | 3                          | 2                          | 0 1                        |
|----------------------------|----------------------------|----------------------------|----------------------------|----------------------------|----------------------------|----------------------------|
| 0                          | 0                          | 0                          | 0                          | 1                          | 0                          | 1 0                        |
| (0) (0) (0) (0) (0) (0) EL | (0) (0) (0) (0) (0) (0) EL | (0) (0) (0) (0) (0) (0) EL | (0) (0) (0) (0) (0) (0) EL | (0) (0) (0) (0) (0) (0) EL | (0) (0) (0) (0) (0) (0) EL | (0) (0) (0) (0) (0) (0) EL |
| VALUE[7:0]                 | VALUE[7:0]                 | VALUE[7:0]                 | VALUE[7:0]                 | VALUE[7:0]                 | VALUE[7:0]                 | VALUE[7:0]                 |
| VALUE[15:8]                | VALUE[15:8]                | VALUE[15:8]                | VALUE[15:8]                | VALUE[15:8]                | VALUE[15:8]                | VALUE[15:8]                |
| VALUE[23:16]               | VALUE[23:16]               | VALUE[23:16]               | VALUE[23:16]               | VALUE[23:16]               | VALUE[23:16]               | VALUE[23:16]               |
| VALUE[31:24]               | VALUE[31:24]               | VALUE[31:24]               | VALUE[31:24]               | VALUE[31:24]               | VALUE[31:24]               | VALUE[31:24]               |
| VALUE[39:32]               | VALUE[39:32]               | VALUE[39:32]               | VALUE[39:32]               | VALUE[39:32]               | VALUE[39:32]               | VALUE[39:32]               |
| VALUE[47:40]               | VALUE[47:40]               | VALUE[47:40]               | VALUE[47:40]               | VALUE[47:40]               | VALUE[47:40]               | VALUE[47:40]               |
| VALUE[55:48]               | VALUE[55:48]               | VALUE[55:48]               | VALUE[55:48]               | VALUE[55:48]               | VALUE[55:48]               | VALUE[55:48]               |
| VALUE[63:56]               | VALUE[63:56]               | VALUE[63:56]               | VALUE[63:56]               | VALUE[63:56]               | VALUE[63:56]               | VALUE[63:56]               |

## D5.3.39 Mispredict Packet

## Purpose

Configurations

Indicates 0-2 E or N Atom elements followed by one Mispredict element .

All.

Packet Layout

## Field descriptions

A

Indicates the number of Atom elements that occurred before the Mispredict element .

The encoding for this field is POD.

| A    | Description                                                     |
|------|-----------------------------------------------------------------|
| 0b00 | 1. Mispredict element .                                         |
| 0b01 | 1. E Atom element . 2. Mispredict element .                     |
| 0b10 | 1. E Atom element . 2. E Atom element . 3. Mispredict element . |
| 0b11 | 1. N Atom element . 2. Mispredict element .                     |

## Additional information

For more information about the decoding of this packet see MispredictPacket().

Figure D5-54 Mispredict Packet

<!-- image -->

## D5.3.40 Overflow Packet

## Purpose

## Configurations

Indicates that a trace unit buffer overflow has occurred.

All.

Indicates that a trace unit buffer overflow has occurred and data might have been lost.

## Packet Layout

## Element sequence

This packet encodes the following sequence:

1. Overflow element .
2. Discard element .

## Additional information

For more information about the decoding of this packet see OverflowPacket().

Figure D5-55 Overflow Packet

## D5.3.41 PE Reset Packet

Purpose

Configurations

Indicates that a PE Reset has occurred.

All.

Packet Layout

## Field descriptions

E

Identifies the elements that are indicated by this packet.

The encoding for this field is POD.

| E    | Description                                                                    |
|------|--------------------------------------------------------------------------------|
| 0b01 | 1. Exception element (PE_Reset, UNKNOWN).                                      |
| 0b10 | 1. Target Address element (UNKNOWN). 2. Exception element (PE_Reset, UNKNOWN). |

All other values are reserved. Reserved values might be defined in a future version of the architecture.

## Additional information

For more information about the decoding of this packet see Parse\_ExceptionPacket().

For more information about the generation of this packet see Address compression.

Figure D5-56 PE Reset Packet

<!-- image -->

## D5.3.42 Q 32-bit address IS0 Packet

## Purpose

Indicates that some instructions have executed with an address of the next instruction.

All.

## Packet Layout

## Field descriptions

A

Instruction virtual address.

Instruction virtual address bits[1:0] always have the value 0b00.

The address is compressed relative to address history buffer entry 0.

The encoding for this field is Bit replacement.

Continuation Bit.

The encoding for this field is Unary code.

| C0   | Description                                     |
|------|-------------------------------------------------|
| 0b0  | Last byte in this section.                      |
| 0b1  | At least one more byte follows in this section. |

## COUNT

Configurations

C0

The number of instructions executed.

The encoding for this field is unsigned LE128n.

Figure D5-57 Q 32-bit address IS0 Packet

| ⠰⤠       | 䅛㠺㉝      | 䅛㠺㉝      | 䅛㠺㉝      | 䅛㠺㉝    | 䅛㠺㉝    | 䅛㠺㉝    |
|----------|----------|----------|----------|--------|--------|--------|
| ⠰⤠       | 䅛ㄵ㨹      | 䅛ㄵ㨹      | 䅛ㄵ㨹      | 䅛ㄵ㨹    | 䅛ㄵ㨹    | 䅛ㄵ㨹    |
| 䅛㈳㨱㙝     | 䅛㈳㨱㙝     | 䅛㈳㨱㙝     | 䅛㈳㨱㙝     | 䅛㈳㨱㙝   | 䅛㈳㨱㙝   | 䅛㈳㨱㙝   |
| 䅛㌱㨲㑝     | 䅛㌱㨲㑝     | 䅛㌱㨲㑝     | 䅛㌱㨲㑝     | 䅛㌱㨲㑝   | 䅛㌱㨲㑝   | 䅛㌱㨲㑝   |
| 䌰        | 䍏啎呛㘺そ    | 䍏啎呛㘺そ    | 䍏啎呛㘺そ    | 䍏啎呛㘺そ  | 䍏啎呛㘺そ  | 䍏啎呛㘺そ  |
| 䌰        | 䍏啎呛ㄳ㨷    | 䍏啎呛ㄳ㨷    | 䍏啎呛ㄳ㨷    | 䍏啎呛ㄳ㨷  | 䍏啎呛ㄳ㨷  | 䍏啎呛ㄳ㨷  |
| 䌰        | 䍏啎呛㈰㨱㑝   | 䍏啎呛㈰㨱㑝   | 䍏啎呛㈰㨱㑝   | 䍏啎呛㈰㨱㑝 | 䍏啎呛㈰㨱㑝 | 䍏啎呛㈰㨱㑝 |
| 䌰        | 䍏啎呛㈷㨲ㅝ   | 䍏啎呛㈷㨲ㅝ   | 䍏啎呛㈷㨲ㅝ   | 䍏啎呛㈷㨲ㅝ | 䍏啎呛㈷㨲ㅝ | 䍏啎呛㈷㨲ㅝ |
| ⠰⤠⠰⤠⠰⤠⠰⤠ | ⠰⤠⠰⤠⠰⤠⠰⤠ | ⠰⤠⠰⤠⠰⤠⠰⤠ | ⠰⤠⠰⤠⠰⤠⠰⤠ | 䍏啎呛㌱㨲㡝 |        |        |

## Element sequence

This packet encodes the following sequence:

1. Qelement .
2. Target Address element .

## Additional information

For more information about the decoding of this packet see Parse\_QPacket().

For more information about the encoding of this packet see Instruction set encoding.

## D5.3.43 Q 32-bit address IS1 Packet

## Purpose

Indicates that some instructions have executed with an address of the next instruction.

All.

## Packet Layout

## Field descriptions

A

Instruction virtual address.

Instruction virtual address bit[0] always has the value 0b0.

The address is compressed relative to address history buffer entry 0.

The encoding for this field is Bit replacement.

Continuation Bit.

The encoding for this field is Unary code.

| C0   | Description                                     |
|------|-------------------------------------------------|
| 0b0  | Last byte in this section.                      |
| 0b1  | At least one more byte follows in this section. |

## COUNT

Configurations

C0

The number of instructions executed.

The encoding for this field is unsigned LE128n.

Figure D5-58 Q 32-bit address IS1 Packet

| ⠰⤠       | 䅛㜺ㅝ      | 䅛㜺ㅝ      | 䅛㜺ㅝ      | 䅛㜺ㅝ    | 䅛㜺ㅝ    | 䅛㜺ㅝ    |
|----------|----------|----------|----------|--------|--------|--------|
| 䅛ㄵ㨸      | 䅛ㄵ㨸      | 䅛ㄵ㨸      | 䅛ㄵ㨸      | 䅛ㄵ㨸    | 䅛ㄵ㨸    | 䅛ㄵ㨸    |
| 䅛㈳㨱㙝     | 䅛㈳㨱㙝     | 䅛㈳㨱㙝     | 䅛㈳㨱㙝     | 䅛㈳㨱㙝   | 䅛㈳㨱㙝   | 䅛㈳㨱㙝   |
| 䅛㌱㨲㑝     | 䅛㌱㨲㑝     | 䅛㌱㨲㑝     | 䅛㌱㨲㑝     | 䅛㌱㨲㑝   | 䅛㌱㨲㑝   | 䅛㌱㨲㑝   |
| 䌰        | 䍏啎呛㘺そ    | 䍏啎呛㘺そ    | 䍏啎呛㘺そ    | 䍏啎呛㘺そ  | 䍏啎呛㘺そ  | 䍏啎呛㘺そ  |
| 䌰        | 䍏啎呛ㄳ㨷    | 䍏啎呛ㄳ㨷    | 䍏啎呛ㄳ㨷    | 䍏啎呛ㄳ㨷  | 䍏啎呛ㄳ㨷  | 䍏啎呛ㄳ㨷  |
| 䌰        | 䍏啎呛㈰㨱㑝   | 䍏啎呛㈰㨱㑝   | 䍏啎呛㈰㨱㑝   | 䍏啎呛㈰㨱㑝 | 䍏啎呛㈰㨱㑝 | 䍏啎呛㈰㨱㑝 |
| 䌰        | 䍏啎呛㈷㨲ㅝ   | 䍏啎呛㈷㨲ㅝ   | 䍏啎呛㈷㨲ㅝ   | 䍏啎呛㈷㨲ㅝ | 䍏啎呛㈷㨲ㅝ | 䍏啎呛㈷㨲ㅝ |
| ⠰⤠⠰⤠⠰⤠⠰⤠ | ⠰⤠⠰⤠⠰⤠⠰⤠ | ⠰⤠⠰⤠⠰⤠⠰⤠ | ⠰⤠⠰⤠⠰⤠⠰⤠ | 䍏啎呛㌱㨲㡝 |        |        |

## Element sequence

This packet encodes the following sequence:

1. Qelement .
2. Target Address element .

## Additional information

For more information about the decoding of this packet see Parse\_QPacket().

For more information about the encoding of this packet see Instruction set encoding.

## D5.3.44 Q Packet

## Purpose

Configurations

Indicates that some instructions have executed, without a count of the number of instructions.

All.

Packet Layout

## Element sequence

This packet encodes the following sequence:

1. Qelement .

## Additional information

For more information about the decoding of this packet see Parse\_QPacket().

Figure D5-59 Q Packet

<!-- image -->

## D5.3.45 Q short address IS0 Packet

## Purpose

Indicates that some instructions have executed with an address of the next instruction.

All.

Packet Layout

## Field descriptions

A

Instruction virtual address.

Instruction virtual address bits[1:0] always have the value 0b00.

The address is compressed relative to address history buffer entry 0.

The encoding for this field is Bit replacement.

Continuation Bit.

The encoding for this field is Unary code.

| C0   | Description                                     |
|------|-------------------------------------------------|
| 0b0  | Last byte in this section.                      |
| 0b1  | At least one more byte follows in this section. |

C1

Configurations

C0

Continuation Bit.

The encoding for this field is Unary code.

Figure D5-60 Q short address IS0 Packet

| 䌰        | 䅛㠺㉝      | 䅛㠺㉝      | 䅛㠺㉝      | 䅛㠺㉝    | 䅛㠺㉝    | 䅛㠺㉝    |
|----------|----------|----------|----------|--------|--------|--------|
| 䅛ㄶ㨹      | 䅛ㄶ㨹      | 䅛ㄶ㨹      | 䅛ㄶ㨹      | 䅛ㄶ㨹    | 䅛ㄶ㨹    | 䅛ㄶ㨹    |
| 䌱        | 䍏啎呛㘺そ    | 䍏啎呛㘺そ    | 䍏啎呛㘺そ    | 䍏啎呛㘺そ  | 䍏啎呛㘺そ  | 䍏啎呛㘺そ  |
| 䌱        | 䍏啎呛ㄳ㨷    | 䍏啎呛ㄳ㨷    | 䍏啎呛ㄳ㨷    | 䍏啎呛ㄳ㨷  | 䍏啎呛ㄳ㨷  | 䍏啎呛ㄳ㨷  |
| 䌱        | 䍏啎呛㈰㨱㑝   | 䍏啎呛㈰㨱㑝   | 䍏啎呛㈰㨱㑝   | 䍏啎呛㈰㨱㑝 | 䍏啎呛㈰㨱㑝 | 䍏啎呛㈰㨱㑝 |
| 䌱        | 䍏啎呛㈷㨲ㅝ   | 䍏啎呛㈷㨲ㅝ   | 䍏啎呛㈷㨲ㅝ   | 䍏啎呛㈷㨲ㅝ | 䍏啎呛㈷㨲ㅝ | 䍏啎呛㈷㨲ㅝ |
| ⠰⤠⠰⤠⠰⤠⠰⤠ | ⠰⤠⠰⤠⠰⤠⠰⤠ | ⠰⤠⠰⤠⠰⤠⠰⤠ | ⠰⤠⠰⤠⠰⤠⠰⤠ | 䍏啎呛㌱㨲㡝 |        |        |

| C1   | Description                                     |
|------|-------------------------------------------------|
| 0b0  | Last byte in this section.                      |
| 0b1  | At least one more byte follows in this section. |

## COUNT

The number of instructions executed.

The encoding for this field is unsigned LE128n.

## Element sequence

This packet encodes the following sequence:

1. Qelement .
2. Target Address element .

## Additional information

For more information about the decoding of this packet see Parse\_QPacket().

For more information about the generation of this packet see Address compression.

For more information about the encoding of this packet see Instruction set encoding.

## D5.3.46 Q short address IS1 Packet

## Purpose

Indicates that some instructions have executed with an address of the next instruction.

All.

Packet Layout

## Field descriptions

A

Instruction virtual address.

Instruction virtual address bit[0] always has the value 0b0.

The address is compressed relative to address history buffer entry 0.

The encoding for this field is Bit replacement.

Continuation Bit.

The encoding for this field is Unary code.

| C0   | Description                                     |
|------|-------------------------------------------------|
| 0b0  | Last byte in this section.                      |
| 0b1  | At least one more byte follows in this section. |

C1

Configurations

C0

Continuation Bit.

The encoding for this field is Unary code.

Figure D5-61 Q short address IS1 Packet

| 䌰        | 䅛㜺ㅝ      | 䅛㜺ㅝ      | 䅛㜺ㅝ      | 䅛㜺ㅝ    | 䅛㜺ㅝ    | 䅛㜺ㅝ    |
|----------|----------|----------|----------|--------|--------|--------|
| 䅛ㄵ㨸      | 䅛ㄵ㨸      | 䅛ㄵ㨸      | 䅛ㄵ㨸      | 䅛ㄵ㨸    | 䅛ㄵ㨸    | 䅛ㄵ㨸    |
| 䌱        | 䍏啎呛㘺そ    | 䍏啎呛㘺そ    | 䍏啎呛㘺そ    | 䍏啎呛㘺そ  | 䍏啎呛㘺そ  | 䍏啎呛㘺そ  |
| 䌱        | 䍏啎呛ㄳ㨷    | 䍏啎呛ㄳ㨷    | 䍏啎呛ㄳ㨷    | 䍏啎呛ㄳ㨷  | 䍏啎呛ㄳ㨷  | 䍏啎呛ㄳ㨷  |
| 䌱        | 䍏啎呛㈰㨱㑝   | 䍏啎呛㈰㨱㑝   | 䍏啎呛㈰㨱㑝   | 䍏啎呛㈰㨱㑝 | 䍏啎呛㈰㨱㑝 | 䍏啎呛㈰㨱㑝 |
| 䌱        | 䍏啎呛㈷㨲ㅝ   | 䍏啎呛㈷㨲ㅝ   | 䍏啎呛㈷㨲ㅝ   | 䍏啎呛㈷㨲ㅝ | 䍏啎呛㈷㨲ㅝ | 䍏啎呛㈷㨲ㅝ |
| ⠰⤠⠰⤠⠰⤠⠰⤠ | ⠰⤠⠰⤠⠰⤠⠰⤠ | ⠰⤠⠰⤠⠰⤠⠰⤠ | ⠰⤠⠰⤠⠰⤠⠰⤠ | 䍏啎呛㌱㨲㡝 |        |        |

| C1   | Description                                     |
|------|-------------------------------------------------|
| 0b0  | Last byte in this section.                      |
| 0b1  | At least one more byte follows in this section. |

## COUNT

The number of instructions executed.

The encoding for this field is unsigned LE128n.

## Element sequence

This packet encodes the following sequence:

1. Qelement .
2. Target Address element .

## Additional information

For more information about the decoding of this packet see Parse\_QPacket().

For more information about the generation of this packet see Address compression.

For more information about the encoding of this packet see Instruction set encoding.

## D5.3.47 Q with count Packet

## Purpose

Indicates that some instructions have executed.

Configurations

All.

Packet Layout

Field descriptions

C0

Continuation Bit.

The encoding for this field is Unary code.

| C0   | Description                                     |
|------|-------------------------------------------------|
| 0b0  | Last byte in this section.                      |
| 0b1  | At least one more byte follows in this section. |

## COUNT

The number of instructions executed.

The encoding for this field is unsigned LE128n.

## Element sequence

This packet encodes the following sequence:

1. Qelement .

## Additional information

For more information about the decoding of this packet see Parse\_QPacket().

| 䌰        | 䍏啎呛㘺そ    | 䍏啎呛㘺そ    | 䍏啎呛㘺そ    | 䍏啎呛㘺そ   | 䍏啎呛㘺そ   | 䍏啎呛㘺そ   |
|----------|----------|----------|----------|---------|---------|---------|
| 䌰        | 䍏啎呛ㄳ㨷    | 䍏啎呛ㄳ㨷    | 䍏啎呛ㄳ㨷    | 䍏啎呛ㄳ㨷   | 䍏啎呛ㄳ㨷   | 䍏啎呛ㄳ㨷   |
| 䌰        | 䍏啎呛㈰㨱㑝   | 䍏啎呛㈰㨱㑝   | 䍏啎呛㈰㨱㑝   | 䍏啎呛㈰㨱㑝  | 䍏啎呛㈰㨱㑝  | 䍏啎呛㈰㨱㑝  |
| 䌰        | 䍏啎呛㈷㨲ㅝ   | 䍏啎呛㈷㨲ㅝ   | 䍏啎呛㈷㨲ㅝ   | 䍏啎呛㈷㨲ㅝ  | 䍏啎呛㈷㨲ㅝ  | 䍏啎呛㈷㨲ㅝ  |
| ⠰⤠⠰⤠⠰⤠⠰⤠ | ⠰⤠⠰⤠⠰⤠⠰⤠ | ⠰⤠⠰⤠⠰⤠⠰⤠ | ⠰⤠⠰⤠⠰⤠⠰⤠ | 䍏啎呛㌱㨲㡝  |         |         |

Figure D5-62 Q with count Packet

## D5.3.48 Q with Exact match address Packet

Purpose

Configurations

Indicates that some instructions have executed with an address of the next instruction.

All.

Packet Layout

Field descriptions

C0

Continuation Bit.

The encoding for this field is Unary code.

| C0   | Description                                     |
|------|-------------------------------------------------|
| 0b0  | Last byte in this section.                      |
| 0b1  | At least one more byte follows in this section. |

## COUNT

The number of instructions executed.

The encoding for this field is unsigned LE128n.

TYPE

The TYPE field indicates what form the rest of the Packet takes.

The encoding for this field is POD.

| TYPE   | Description                                                                                                                      |
|--------|----------------------------------------------------------------------------------------------------------------------------------|
| 0b00   | Apacket with this TYPE value also indicates a Target Address element with an address the same as address history buffer entry 0. |
| 0b01   | Apacket with this TYPE value also indicates a Target Address element with an address the same as address history buffer entry 1. |

Figure D5-63 Q with Exact match address Packet

|          |          |          | 呙偅       |        |        |
|----------|----------|----------|----------|--------|--------|
| 䌰        | 䍏啎呛㘺そ    | 䍏啎呛㘺そ    | 䍏啎呛㘺そ    | 䍏啎呛㘺そ  | 䍏啎呛㘺そ  |
| 䌰        | 䍏啎呛ㄳ㨷    | 䍏啎呛ㄳ㨷    | 䍏啎呛ㄳ㨷    | 䍏啎呛ㄳ㨷  | 䍏啎呛ㄳ㨷  |
| 䌰        | 䍏啎呛㈰㨱㑝   | 䍏啎呛㈰㨱㑝   | 䍏啎呛㈰㨱㑝   | 䍏啎呛㈰㨱㑝 | 䍏啎呛㈰㨱㑝 |
| 䌰        | 䍏啎呛㈷㨲ㅝ   | 䍏啎呛㈷㨲ㅝ   | 䍏啎呛㈷㨲ㅝ   | 䍏啎呛㈷㨲ㅝ | 䍏啎呛㈷㨲ㅝ |
| ⠰⤠⠰⤠⠰⤠⠰⤠ | ⠰⤠⠰⤠⠰⤠⠰⤠ | ⠰⤠⠰⤠⠰⤠⠰⤠ | ⠰⤠⠰⤠⠰⤠⠰⤠ |        |        |

| TYPE   | Description                                                                                                                      |
|--------|----------------------------------------------------------------------------------------------------------------------------------|
| 0b10   | Apacket with this TYPE value also indicates a Target Address element with an address the same as address history buffer entry 2. |
| 0b11   | RESERVED                                                                                                                         |

## Element sequence

This packet encodes the following sequence:

1. Qelement .
2. Target Address element .

## Additional information

For more information about the decoding of this packet see Parse\_QPacket().

For more information about the generation of this packet see Address compression.

## D5.3.49 Source Address 32-bit IS0 Packet

## Purpose

Indicates the source address of a P0 instruction , and that the instruction was taken.

All.

## Packet Layout

## Field descriptions

A

Instruction virtual address.

Instruction virtual address bits[1:0] always have the value 0b00.

The address is compressed relative to address history buffer entry 0.

The encoding for this field is Bit replacement.

## Element sequence

This packet encodes the following sequence:

1. Source Address element .

## Additional information

For more information about the decoding of this packet see Parse\_SourceAddressPacket().

For more information about the generation of this packet see Address compression.

For more information about the encoding of this packet see Instruction set encoding.

## Configurations

Figure D5-64 Source Address 32-bit IS0 Packet

| ⠰⤠   | 䅛㠺㉝   | 䅛㠺㉝   | 䅛㠺㉝   | 䅛㠺㉝   | 䅛㠺㉝   | 䅛㠺㉝   |
|------|-------|-------|-------|-------|-------|-------|
| ⠰⤠   | 䅛ㄵ㨹   | 䅛ㄵ㨹   | 䅛ㄵ㨹   | 䅛ㄵ㨹   | 䅛ㄵ㨹   | 䅛ㄵ㨹   |
| 䅛㈳㨱㙝 | 䅛㈳㨱㙝  | 䅛㈳㨱㙝  | 䅛㈳㨱㙝  | 䅛㈳㨱㙝  | 䅛㈳㨱㙝  | 䅛㈳㨱㙝  |
| 䅛㌱㨲㑝 | 䅛㌱㨲㑝  | 䅛㌱㨲㑝  | 䅛㌱㨲㑝  | 䅛㌱㨲㑝  | 䅛㌱㨲㑝  | 䅛㌱㨲㑝  |

## D5.3.50 Source Address 32-bit IS1 Packet

## Purpose

Indicates the source address of a P0 instruction , and that the instruction was taken.

All.

## Packet Layout

## Field descriptions

A

Instruction virtual address.

Instruction virtual address bit[0] always has the value 0b0.

The address is compressed relative to address history buffer entry 0.

The encoding for this field is Bit replacement.

## Element sequence

This packet encodes the following sequence:

1. Source Address element .

## Additional information

For more information about the decoding of this packet see Parse\_SourceAddressPacket().

For more information about the generation of this packet see Address compression.

For more information about the encoding of this packet see Instruction set encoding.

## Configurations

Figure D5-65 Source Address 32-bit IS1 Packet

| ⠰⤠   | 䅛㜺ㅝ   | 䅛㜺ㅝ   | 䅛㜺ㅝ   | 䅛㜺ㅝ   | 䅛㜺ㅝ   | 䅛㜺ㅝ   |
|------|-------|-------|-------|-------|-------|-------|
| 䅛ㄵ㨸  | 䅛ㄵ㨸   | 䅛ㄵ㨸   | 䅛ㄵ㨸   | 䅛ㄵ㨸   | 䅛ㄵ㨸   | 䅛ㄵ㨸   |
| 䅛㈳㨱㙝 | 䅛㈳㨱㙝  | 䅛㈳㨱㙝  | 䅛㈳㨱㙝  | 䅛㈳㨱㙝  | 䅛㈳㨱㙝  | 䅛㈳㨱㙝  |
| 䅛㌱㨲㑝 | 䅛㌱㨲㑝  | 䅛㌱㨲㑝  | 䅛㌱㨲㑝  | 䅛㌱㨲㑝  | 䅛㌱㨲㑝  | 䅛㌱㨲㑝  |

## D5.3.51 Source Address 64-bit IS0 Packet

## Purpose

Indicates the source address of a P0 instruction , and that the instruction was taken.

All.

## Packet Layout

## Field descriptions

A

Instruction virtual address.

Instruction virtual address bits[1:0] always have the value 0b00.

The address is compressed relative to address history buffer entry 0.

The encoding for this field is Bit replacement.

## Element sequence

This packet encodes the following sequence:

1. Source Address element .

## Additional information

For more information about the decoding of this packet see Parse\_SourceAddressPacket().

For more information about the generation of this packet see Address compression.

For more information about the encoding of this packet see Instruction set encoding.

## Configurations

Figure D5-66 Source Address 64-bit IS0 Packet

| ⠰⤠   | 䅛㠺㉝   | 䅛㠺㉝   | 䅛㠺㉝   | 䅛㠺㉝   | 䅛㠺㉝   | 䅛㠺㉝   | 䅛㠺㉝   |
|------|-------|-------|-------|-------|-------|-------|-------|
| ⠰⤠   | 䅛ㄵ㨹   | 䅛ㄵ㨹   | 䅛ㄵ㨹   | 䅛ㄵ㨹   | 䅛ㄵ㨹   | 䅛ㄵ㨹   | 䅛ㄵ㨹   |
| 䅛㈳㨱㙝 | 䅛㈳㨱㙝  | 䅛㈳㨱㙝  | 䅛㈳㨱㙝  | 䅛㈳㨱㙝  | 䅛㈳㨱㙝  | 䅛㈳㨱㙝  | 䅛㈳㨱㙝  |
| 䅛㌱㨲㑝 | 䅛㌱㨲㑝  | 䅛㌱㨲㑝  | 䅛㌱㨲㑝  | 䅛㌱㨲㑝  | 䅛㌱㨲㑝  | 䅛㌱㨲㑝  | 䅛㌱㨲㑝  |
| 䅛㌹㨳㉝ | 䅛㌹㨳㉝  | 䅛㌹㨳㉝  | 䅛㌹㨳㉝  | 䅛㌹㨳㉝  | 䅛㌹㨳㉝  | 䅛㌹㨳㉝  | 䅛㌹㨳㉝  |
| 䅛㐷㨴そ | 䅛㐷㨴そ  | 䅛㐷㨴そ  | 䅛㐷㨴そ  | 䅛㐷㨴そ  | 䅛㐷㨴そ  | 䅛㐷㨴そ  | 䅛㐷㨴そ  |
| 䅛㔵㨴㡝 | 䅛㔵㨴㡝  | 䅛㔵㨴㡝  | 䅛㔵㨴㡝  | 䅛㔵㨴㡝  | 䅛㔵㨴㡝  | 䅛㔵㨴㡝  | 䅛㔵㨴㡝  |
| 䅛㘳㨵㙝 | 䅛㘳㨵㙝  | 䅛㘳㨵㙝  | 䅛㘳㨵㙝  | 䅛㘳㨵㙝  | 䅛㘳㨵㙝  | 䅛㘳㨵㙝  | 䅛㘳㨵㙝  |

## D5.3.52 Source Address 64-bit IS1 Packet

## Purpose

Indicates the source address of a P0 instruction , and that the instruction was taken.

All.

## Packet Layout

## Field descriptions

A

Instruction virtual address.

Instruction virtual address bit[0] always has the value 0b0.

The address is compressed relative to address history buffer entry 0.

The encoding for this field is Bit replacement.

## Element sequence

This packet encodes the following sequence:

1. Source Address element .

## Additional information

For more information about the decoding of this packet see Parse\_SourceAddressPacket().

For more information about the generation of this packet see Address compression.

For more information about the encoding of this packet see Instruction set encoding.

## Configurations

Figure D5-67 Source Address 64-bit IS1 Packet

| ⠰⤠   | 䅛㜺ㅝ   | 䅛㜺ㅝ   | 䅛㜺ㅝ   | 䅛㜺ㅝ   | 䅛㜺ㅝ   | 䅛㜺ㅝ   |
|------|-------|-------|-------|-------|-------|-------|
| 䅛ㄵ㨸  | 䅛ㄵ㨸   | 䅛ㄵ㨸   | 䅛ㄵ㨸   | 䅛ㄵ㨸   | 䅛ㄵ㨸   | 䅛ㄵ㨸   |
| 䅛㈳㨱㙝 | 䅛㈳㨱㙝  | 䅛㈳㨱㙝  | 䅛㈳㨱㙝  | 䅛㈳㨱㙝  | 䅛㈳㨱㙝  | 䅛㈳㨱㙝  |
| 䅛㌱㨲㑝 | 䅛㌱㨲㑝  | 䅛㌱㨲㑝  | 䅛㌱㨲㑝  | 䅛㌱㨲㑝  | 䅛㌱㨲㑝  | 䅛㌱㨲㑝  |
| 䅛㌹㨳㉝ | 䅛㌹㨳㉝  | 䅛㌹㨳㉝  | 䅛㌹㨳㉝  | 䅛㌹㨳㉝  | 䅛㌹㨳㉝  | 䅛㌹㨳㉝  |
| 䅛㐷㨴そ | 䅛㐷㨴そ  | 䅛㐷㨴そ  | 䅛㐷㨴そ  | 䅛㐷㨴そ  | 䅛㐷㨴そ  | 䅛㐷㨴そ  |
| 䅛㔵㨴㡝 | 䅛㔵㨴㡝  | 䅛㔵㨴㡝  | 䅛㔵㨴㡝  | 䅛㔵㨴㡝  | 䅛㔵㨴㡝  | 䅛㔵㨴㡝  |
| 䅛㘳㨵㙝 | 䅛㘳㨵㙝  | 䅛㘳㨵㙝  | 䅛㘳㨵㙝  | 䅛㘳㨵㙝  | 䅛㘳㨵㙝  | 䅛㘳㨵㙝  |

## D5.3.53 Source Address Exact Match Packet

## Purpose

Configurations

Indicates the source address of a P0 instruction , and that the instruction was taken.

All.

Packet Layout

## Field descriptions

QE

Instruction virtual address.

The encoding for this field is POD.

| QE   | Description                                                |
|------|------------------------------------------------------------|
| 0b00 | The address is the same as address history buffer entry 0. |
| 0b01 | The address is the same as address history buffer entry 1. |
| 0b10 | The address is the same as address history buffer entry 2. |

## Element sequence

This packet encodes the following sequence:

1. Source Address element .

## Additional information

For more information about the decoding of this packet see Parse\_SourceAddressPacket().

For more information about the generation of this packet see Address compression.

Figure D5-68 Source Address Exact Match Packet

<!-- image -->

## D5.3.54 Source Address Short IS0 Packet

## Purpose

Indicates the source address of a P0 instruction , and that the instruction was taken.

All.

## Packet Layout

## Field descriptions

A

Instruction virtual address.

Instruction virtual address bits[1:0] always have the value 0b00.

The address is compressed relative to address history buffer entry 0.

The encoding for this field is Bit replacement.

Continuation Bit.

The encoding for this field is Unary code.

| C0   | Description                                     |
|------|-------------------------------------------------|
| 0b0  | Last byte in this section.                      |
| 0b1  | At least one more byte follows in this section. |

## Element sequence

This packet encodes the following sequence:

1. Source Address element .

## Additional information

For more information about the decoding of this packet see Parse\_SourceAddressPacket().

For more information about the generation of this packet see Address compression.

For more information about the encoding of this packet see Instruction set encoding.

## Configurations

C0

Figure D5-69 Source Address Short IS0 Packet

<!-- image -->

## D5.3.55 Source Address Short IS1 Packet

## Purpose

Indicates the source address of a P0 instruction , and that the instruction was taken.

All.

## Packet Layout

## Field descriptions

A

Instruction virtual address.

Instruction virtual address bit[0] always has the value 0b0.

The address is compressed relative to address history buffer entry 0.

The encoding for this field is Bit replacement.

Continuation Bit.

The encoding for this field is Unary code.

| C0   | Description                                     |
|------|-------------------------------------------------|
| 0b0  | Last byte in this section.                      |
| 0b1  | At least one more byte follows in this section. |

## Element sequence

This packet encodes the following sequence:

1. Source Address element .

## Additional information

For more information about the decoding of this packet see Parse\_SourceAddressPacket().

For more information about the generation of this packet see Address compression.

For more information about the encoding of this packet see Instruction set encoding.

## Configurations

C0

Figure D5-70 Source Address Short IS1 Packet

<!-- image -->

## D5.3.56 Timestamp Marker Packet

Purpose

Indicates a Timestamp Marker element .

TRCIDR0.TSSIZE != 0b00000 and TRCIDR0.TSMARK == 0b1

Figure D5-71 Timestamp Marker Packet

<!-- image -->

Configurations

Packet Layout

## D5.3.57 Timestamp Packet

Purpose

Configurations

TRCIDR0.TSSIZE != 0b00000.

Packet Layout - Variant 1

Packet Layout - Variant 2

Field descriptions

C0

Continuation Bit.

The encoding for this field is Unary code.

Indicates a Timestamp element .

Figure D5-72 Timestamp Packet (1)

| 䌰    | 呓嬶㨰   | 呓嬶㨰   | 呓嬶㨰   | 呓嬶㨰   | 呓嬶㨰   | 呓嬶㨰   | 呓嬶㨰   |
|------|-------|-------|-------|-------|-------|-------|-------|
| 䌰    | 呓嬱㌺㝝  | 呓嬱㌺㝝  | 呓嬱㌺㝝  | 呓嬱㌺㝝  | 呓嬱㌺㝝  | 呓嬱㌺㝝  | 呓嬱㌺㝝  |
| 䌰    | 呓嬲〺ㄴ  | 呓嬲〺ㄴ  | 呓嬲〺ㄴ  | 呓嬲〺ㄴ  | 呓嬲〺ㄴ  | 呓嬲〺ㄴ  | 呓嬲〺ㄴ  |
| 䌰    | 呓嬲㜺㈱  | 呓嬲㜺㈱  | 呓嬲㜺㈱  | 呓嬲㜺㈱  | 呓嬲㜺㈱  | 呓嬲㜺㈱  | 呓嬲㜺㈱  |
| 䌰    | 呓嬳㐺㈸  | 呓嬳㐺㈸  | 呓嬳㐺㈸  | 呓嬳㐺㈸  | 呓嬳㐺㈸  | 呓嬳㐺㈸  | 呓嬳㐺㈸  |
| 䌰    | 呓嬴ㄺ㌵  | 呓嬴ㄺ㌵  | 呓嬴ㄺ㌵  | 呓嬴ㄺ㌵  | 呓嬴ㄺ㌵  | 呓嬴ㄺ㌵  | 呓嬴ㄺ㌵  |
| 䌰    | 呓嬴㠺㐲  | 呓嬴㠺㐲  | 呓嬴㠺㐲  | 呓嬴㠺㐲  | 呓嬴㠺㐲  | 呓嬴㠺㐲  | 呓嬴㠺㐲  |
| 䌰    | 呓嬵㔺㐹  | 呓嬵㔺㐹  | 呓嬵㔺㐹  | 呓嬵㔺㐹  | 呓嬵㔺㐹  | 呓嬵㔺㐹  | 呓嬵㔺㐹  |
| 呓嬶㌺㔶 | 呓嬶㌺㔶  | 呓嬶㌺㔶  | 呓嬶㌺㔶  | 呓嬶㌺㔶  | 呓嬶㌺㔶  | 呓嬶㌺㔶  | 呓嬶㌺㔶  |

Figure D5-73 Timestamp Packet (2)

| 䌰    | 呓嬶㨰   | 呓嬶㨰    | 呓嬶㨰    | 呓嬶㨰    | 呓嬶㨰    | 呓嬶㨰    |
|------|-------|--------|--------|--------|--------|--------|
| 䌰    | 呓嬱㌺㝝  | 呓嬱㌺㝝   | 呓嬱㌺㝝   | 呓嬱㌺㝝   | 呓嬱㌺㝝   | 呓嬱㌺㝝   |
| 䌰    | 呓嬲〺ㄴ  | 呓嬲〺ㄴ   | 呓嬲〺ㄴ   | 呓嬲〺ㄴ   | 呓嬲〺ㄴ   | 呓嬲〺ㄴ   |
| 䌰    | 呓嬲㜺㈱  | 呓嬲㜺㈱   | 呓嬲㜺㈱   | 呓嬲㜺㈱   | 呓嬲㜺㈱   | 呓嬲㜺㈱   |
| 䌰    | 呓嬳㐺㈸  | 呓嬳㐺㈸   | 呓嬳㐺㈸   | 呓嬳㐺㈸   | 呓嬳㐺㈸   | 呓嬳㐺㈸   |
| 䌰    | 呓嬴ㄺ㌵  | 呓嬴ㄺ㌵   | 呓嬴ㄺ㌵   | 呓嬴ㄺ㌵   | 呓嬴ㄺ㌵   | 呓嬴ㄺ㌵   |
| 䌰    | 呓嬴㠺㐲  | 呓嬴㠺㐲   | 呓嬴㠺㐲   | 呓嬴㠺㐲   | 呓嬴㠺㐲   | 呓嬴㠺㐲   |
| 䌰    | 呓嬵㔺㐹  | 呓嬵㔺㐹   | 呓嬵㔺㐹   | 呓嬵㔺㐹   | 呓嬵㔺㐹   | 呓嬵㔺㐹   |
| 呓嬶㌺㔶 | 呓嬶㌺㔶  | 呓嬶㌺㔶   | 呓嬶㌺㔶   | 呓嬶㌺㔶   | 呓嬶㌺㔶   | 呓嬶㌺㔶   |
| 䌱    | 䍏啎呛㘺そ | 䍏啎呛㘺そ  | 䍏啎呛㘺そ  | 䍏啎呛㘺そ  | 䍏啎呛㘺そ  | 䍏啎呛㘺そ  |
| 䌱    | 䍏啎呛ㄳ㨷 | 䍏啎呛ㄳ㨷  | 䍏啎呛ㄳ㨷  | 䍏啎呛ㄳ㨷  | 䍏啎呛ㄳ㨷  | 䍏啎呛ㄳ㨷  |
| ⠰⤠⠰⤠ | ⠰⤠⠰⤠  | 䍏啎呛ㄹ㨱㑝 | 䍏啎呛ㄹ㨱㑝 | 䍏啎呛ㄹ㨱㑝 | 䍏啎呛ㄹ㨱㑝 | 䍏啎呛ㄹ㨱㑝 |

| C0   | Description                                     |
|------|-------------------------------------------------|
| 0b0  | Last byte in this section.                      |
| 0b1  | At least one more byte follows in this section. |

C1

Continuation Bit.

The encoding for this field is Unary code.

| C1   | Description                                     |
|------|-------------------------------------------------|
| 0b0  | Last byte in this section.                      |
| 0b1  | At least one more byte follows in this section. |

## COUNT

TS

The number of PE clock cycles between the most recent Cycle Count element and the element related to the Timestamp. When the COUNT field is not present, the cycle count value is UNKNOWN.

The encoding for this field is unsigned LE128n.

Timestamp Value.

The encoding for this field is Bit replacement.

## Element sequence

This packet encodes the following sequence:

1. Timestamp element .

## Additional information

For more information about the decoding of this packet see TimestampPacket().

## D5.3.58 Target Address 32-bit IS0 Packet

## Purpose

Indicates a Target Address element .

## Configurations

All.

## Packet Layout

## Field descriptions

A

Instruction virtual address.

Instruction virtual address bits[1:0] always have the value 0b00.

The address is compressed relative to address history buffer entry 0.

The encoding for this field is Bit replacement.

## Element sequence

This packet encodes the following sequence:

1. Target Address element .

## Additional information

For more information about the decoding of this packet see Parse\_TargetAddressPacket().

For more information about the generation of this packet see Address compression.

For more information about the encoding of this packet see Instruction set encoding.

Figure D5-74 Target Address 32-bit IS0 Packet

| ⠰⤠   | 䅛㠺㉝   | 䅛㠺㉝   | 䅛㠺㉝   | 䅛㠺㉝   | 䅛㠺㉝   | 䅛㠺㉝   |
|------|-------|-------|-------|-------|-------|-------|
| ⠰⤠   | 䅛ㄵ㨹   | 䅛ㄵ㨹   | 䅛ㄵ㨹   | 䅛ㄵ㨹   | 䅛ㄵ㨹   | 䅛ㄵ㨹   |
| 䅛㈳㨱㙝 | 䅛㈳㨱㙝  | 䅛㈳㨱㙝  | 䅛㈳㨱㙝  | 䅛㈳㨱㙝  | 䅛㈳㨱㙝  | 䅛㈳㨱㙝  |
| 䅛㌱㨲㑝 | 䅛㌱㨲㑝  | 䅛㌱㨲㑝  | 䅛㌱㨲㑝  | 䅛㌱㨲㑝  | 䅛㌱㨲㑝  | 䅛㌱㨲㑝  |

## D5.3.59 Target Address 32-bit IS1 Packet

## Purpose

Indicates a Target Address element .

## Configurations

All.

## Packet Layout

## Field descriptions

A

Instruction virtual address.

Instruction virtual address bit[0] always has the value 0b0.

The address is compressed relative to address history buffer entry 0.

The encoding for this field is Bit replacement.

## Element sequence

This packet encodes the following sequence:

1. Target Address element .

## Additional information

For more information about the decoding of this packet see Parse\_TargetAddressPacket().

For more information about the generation of this packet see Address compression.

For more information about the encoding of this packet see Instruction set encoding.

Figure D5-75 Target Address 32-bit IS1 Packet

| ⠰⤠   | 䅛㜺ㅝ   | 䅛㜺ㅝ   | 䅛㜺ㅝ   | 䅛㜺ㅝ   | 䅛㜺ㅝ   | 䅛㜺ㅝ   |
|------|-------|-------|-------|-------|-------|-------|
| 䅛ㄵ㨸  | 䅛ㄵ㨸   | 䅛ㄵ㨸   | 䅛ㄵ㨸   | 䅛ㄵ㨸   | 䅛ㄵ㨸   | 䅛ㄵ㨸   |
| 䅛㈳㨱㙝 | 䅛㈳㨱㙝  | 䅛㈳㨱㙝  | 䅛㈳㨱㙝  | 䅛㈳㨱㙝  | 䅛㈳㨱㙝  | 䅛㈳㨱㙝  |
| 䅛㌱㨲㑝 | 䅛㌱㨲㑝  | 䅛㌱㨲㑝  | 䅛㌱㨲㑝  | 䅛㌱㨲㑝  | 䅛㌱㨲㑝  | 䅛㌱㨲㑝  |

## D5.3.60 Target Address 64-bit IS0 Packet

## Purpose

Indicates a Target Address element .

All.

## Packet Layout

## Field descriptions

A

Instruction virtual address.

Instruction virtual address bits[1:0] always have the value 0b00.

The address is compressed relative to address history buffer entry 0.

The encoding for this field is Bit replacement.

## Element sequence

This packet encodes the following sequence:

1. Target Address element .

## Additional information

For more information about the decoding of this packet see Parse\_TargetAddressPacket().

For more information about the generation of this packet see Address compression.

For more information about the encoding of this packet see Instruction set encoding.

## Configurations

Figure D5-76 Target Address 64-bit IS0 Packet

| ⠰⤠   | 䅛㠺㉝   | 䅛㠺㉝   | 䅛㠺㉝   | 䅛㠺㉝   | 䅛㠺㉝   | 䅛㠺㉝   |
|------|-------|-------|-------|-------|-------|-------|
| ⠰⤠   | 䅛ㄵ㨹   | 䅛ㄵ㨹   | 䅛ㄵ㨹   | 䅛ㄵ㨹   | 䅛ㄵ㨹   | 䅛ㄵ㨹   |
| 䅛㈳㨱㙝 | 䅛㈳㨱㙝  | 䅛㈳㨱㙝  | 䅛㈳㨱㙝  | 䅛㈳㨱㙝  | 䅛㈳㨱㙝  | 䅛㈳㨱㙝  |
| 䅛㌱㨲㑝 | 䅛㌱㨲㑝  | 䅛㌱㨲㑝  | 䅛㌱㨲㑝  | 䅛㌱㨲㑝  | 䅛㌱㨲㑝  | 䅛㌱㨲㑝  |
| 䅛㌹㨳㉝ | 䅛㌹㨳㉝  | 䅛㌹㨳㉝  | 䅛㌹㨳㉝  | 䅛㌹㨳㉝  | 䅛㌹㨳㉝  | 䅛㌹㨳㉝  |
| 䅛㐷㨴そ | 䅛㐷㨴そ  | 䅛㐷㨴そ  | 䅛㐷㨴そ  | 䅛㐷㨴そ  | 䅛㐷㨴そ  | 䅛㐷㨴そ  |
| 䅛㔵㨴㡝 | 䅛㔵㨴㡝  | 䅛㔵㨴㡝  | 䅛㔵㨴㡝  | 䅛㔵㨴㡝  | 䅛㔵㨴㡝  | 䅛㔵㨴㡝  |
| 䅛㘳㨵㙝 | 䅛㘳㨵㙝  | 䅛㘳㨵㙝  | 䅛㘳㨵㙝  | 䅛㘳㨵㙝  | 䅛㘳㨵㙝  | 䅛㘳㨵㙝  |

## D5.3.61 Target Address 64-bit IS1 Packet

## Purpose

Indicates a Target Address element .

All.

Packet Layout

## Field descriptions

A

Instruction virtual address.

Instruction virtual address bit[0] always has the value 0b0.

The address is compressed relative to address history buffer entry 0.

The encoding for this field is Bit replacement.

## Element sequence

This packet encodes the following sequence:

1. Target Address element .

## Additional information

For more information about the decoding of this packet see Parse\_TargetAddressPacket().

For more information about the generation of this packet see Address compression.

For more information about the encoding of this packet see Instruction set encoding.

## Configurations

Figure D5-77 Target Address 64-bit IS1 Packet

| ⠰⤠   | 䅛㜺ㅝ   | 䅛㜺ㅝ   | 䅛㜺ㅝ   | 䅛㜺ㅝ   | 䅛㜺ㅝ   | 䅛㜺ㅝ   |
|------|-------|-------|-------|-------|-------|-------|
| 䅛ㄵ㨸  | 䅛ㄵ㨸   | 䅛ㄵ㨸   | 䅛ㄵ㨸   | 䅛ㄵ㨸   | 䅛ㄵ㨸   | 䅛ㄵ㨸   |
| 䅛㈳㨱㙝 | 䅛㈳㨱㙝  | 䅛㈳㨱㙝  | 䅛㈳㨱㙝  | 䅛㈳㨱㙝  | 䅛㈳㨱㙝  | 䅛㈳㨱㙝  |
| 䅛㌱㨲㑝 | 䅛㌱㨲㑝  | 䅛㌱㨲㑝  | 䅛㌱㨲㑝  | 䅛㌱㨲㑝  | 䅛㌱㨲㑝  | 䅛㌱㨲㑝  |
| 䅛㌹㨳㉝ | 䅛㌹㨳㉝  | 䅛㌹㨳㉝  | 䅛㌹㨳㉝  | 䅛㌹㨳㉝  | 䅛㌹㨳㉝  | 䅛㌹㨳㉝  |
| 䅛㐷㨴そ | 䅛㐷㨴そ  | 䅛㐷㨴そ  | 䅛㐷㨴そ  | 䅛㐷㨴そ  | 䅛㐷㨴そ  | 䅛㐷㨴そ  |
| 䅛㔵㨴㡝 | 䅛㔵㨴㡝  | 䅛㔵㨴㡝  | 䅛㔵㨴㡝  | 䅛㔵㨴㡝  | 䅛㔵㨴㡝  | 䅛㔵㨴㡝  |
| 䅛㘳㨵㙝 | 䅛㘳㨵㙝  | 䅛㘳㨵㙝  | 䅛㘳㨵㙝  | 䅛㘳㨵㙝  | 䅛㘳㨵㙝  | 䅛㘳㨵㙝  |

## D5.3.62 Target Address Exact Match Packet

## Purpose

Configurations

Indicates a Target Address element .

All.

Packet Layout

## Field descriptions

QE

Instruction virtual address.

The encoding for this field is POD.

| QE   | Description                                                |
|------|------------------------------------------------------------|
| 0b00 | The address is the same as address history buffer entry 0. |
| 0b01 | The address is the same as address history buffer entry 1. |
| 0b10 | The address is the same as address history buffer entry 2. |

## Element sequence

This packet encodes the following sequence:

1. Target Address element .

## Additional information

For more information about the decoding of this packet see Parse\_TargetAddressPacket().

For more information about the generation of this packet see Address compression.

Figure D5-78 Target Address Exact Match Packet

<!-- image -->

## D5.3.63 Target Address Short IS0 Packet

## Purpose

Indicates a Target Address element .

## Configurations

All.

## Packet Layout

## Field descriptions

A

Instruction virtual address.

Instruction virtual address bits[1:0] always have the value 0b00.

The address is compressed relative to address history buffer entry 0.

The encoding for this field is Bit replacement.

Continuation Bit.

The encoding for this field is Unary code.

| C0   | Description                                     |
|------|-------------------------------------------------|
| 0b0  | Last byte in this section.                      |
| 0b1  | At least one more byte follows in this section. |

## Element sequence

This packet encodes the following sequence:

1. Target Address element .

## Additional information

For more information about the decoding of this packet see Parse\_TargetAddressPacket().

For more information about the generation of this packet see Address compression.

For more information about the encoding of this packet see Instruction set encoding.

C0

Figure D5-79 Target Address Short IS0 Packet

<!-- image -->

## D5.3.64 Target Address Short IS1 Packet

## Purpose

Indicates a Target Address element .

## Configurations

All.

## Packet Layout

## Field descriptions

A

Instruction virtual address.

Instruction virtual address bit[0] always has the value 0b0.

The address is compressed relative to address history buffer entry 0.

The encoding for this field is Bit replacement.

Continuation Bit.

The encoding for this field is Unary code.

| C0   | Description                                     |
|------|-------------------------------------------------|
| 0b0  | Last byte in this section.                      |
| 0b1  | At least one more byte follows in this section. |

## Element sequence

This packet encodes the following sequence:

1. Target Address element .

## Additional information

For more information about the decoding of this packet see Parse\_TargetAddressPacket().

For more information about the generation of this packet see Address compression.

For more information about the encoding of this packet see Instruction set encoding.

C0

Figure D5-80 Target Address Short IS1 Packet

<!-- image -->

## D5.3.65 Target Address with Context 32-bit IS0 Packet

Purpose

Configurations

Indicates a Target Address element and a Context element .

All.

Packet Layout - Variant 1

Packet Layout - Variant 2

Figure D5-81 Target Address with Context 32-bit IS0 Packet (1)

<!-- image -->

Figure D5-82 Target Address with Context 32-bit IS0 Packet (2)

<!-- image -->

## Packet Layout - Variant 3

## Packet Layout - Variant 4

## Field descriptions

A

Instruction virtual address.

Instruction virtual address bits[1:0] always have the value 0b00.

The address is compressed relative to address history buffer entry 0.

The encoding for this field is Bit replacement.

## CONTEXTID

Context identifier.

Figure D5-83 Target Address with Context 32-bit IS0 Packet (3)

<!-- image -->

| ⠰⤠    | 䅛㠺㉝   | 䅛㠺㉝   | 䅛㠺㉝   | 䅛㠺㉝   | 䅛㠺㉝   | 䅛㠺㉝   | 䅛㠺㉝   |
|-------|-------|-------|-------|-------|-------|-------|-------|
| ⠰⤠    | 䅛ㄵ㨹   | 䅛ㄵ㨹   | 䅛ㄵ㨹   | 䅛ㄵ㨹   | 䅛ㄵ㨹   | 䅛ㄵ㨹   | 䅛ㄵ㨹   |
| 䅛㈳㨱㙝  | 䅛㈳㨱㙝  | 䅛㈳㨱㙝  | 䅛㈳㨱㙝  | 䅛㈳㨱㙝  | 䅛㈳㨱㙝  | 䅛㈳㨱㙝  | 䅛㈳㨱㙝  |
| 䅛㌱㨲㑝  | 䅛㌱㨲㑝  | 䅛㌱㨲㑝  | 䅛㌱㨲㑝  | 䅛㌱㨲㑝  | 䅛㌱㨲㑝  | 䅛㌱㨲㑝  | 䅛㌱㨲㑝  |
|       |       | 乓     | 卆     | 乓     | ⠰⤠    | 䕌     |       |
| 噍䥄嬷㨰  | 噍䥄嬷㨰  | 噍䥄嬷㨰  | 噍䥄嬷㨰  | 噍䥄嬷㨰  | 噍䥄嬷㨰  | 噍䥄嬷㨰  | 噍䥄嬷㨰  |
| 噍䥄嬱㔺㡝 | 噍䥄嬱㔺㡝 | 噍䥄嬱㔺㡝 | 噍䥄嬱㔺㡝 | 噍䥄嬱㔺㡝 | 噍䥄嬱㔺㡝 | 噍䥄嬱㔺㡝 | 噍䥄嬱㔺㡝 |
| 噍䥄嬲㌺ㄶ | 噍䥄嬲㌺ㄶ | 噍䥄嬲㌺ㄶ | 噍䥄嬲㌺ㄶ | 噍䥄嬲㌺ㄶ | 噍䥄嬲㌺ㄶ | 噍䥄嬲㌺ㄶ | 噍䥄嬲㌺ㄶ |
| 噍䥄嬳ㄺ㈴ | 噍䥄嬳ㄺ㈴ | 噍䥄嬳ㄺ㈴ | 噍䥄嬳ㄺ㈴ | 噍䥄嬳ㄺ㈴ | 噍䥄嬳ㄺ㈴ | 噍䥄嬳ㄺ㈴ | 噍䥄嬳ㄺ㈴ |

Figure D5-84 Target Address with Context 32-bit IS0 Packet (4)

<!-- image -->

| ⠰⤠       | 䅛㠺㉝      | 䅛㠺㉝      | 䅛㠺㉝      | 䅛㠺㉝      | 䅛㠺㉝      | 䅛㠺㉝      | 䅛㠺㉝      |
|----------|----------|----------|----------|----------|----------|----------|----------|
| ⠰⤠       | 䅛ㄵ㨹      | 䅛ㄵ㨹      | 䅛ㄵ㨹      | 䅛ㄵ㨹      | 䅛ㄵ㨹      | 䅛ㄵ㨹      | 䅛ㄵ㨹      |
| 䅛㈳㨱㙝     | 䅛㈳㨱㙝     | 䅛㈳㨱㙝     | 䅛㈳㨱㙝     | 䅛㈳㨱㙝     | 䅛㈳㨱㙝     | 䅛㈳㨱㙝     | 䅛㈳㨱㙝     |
| 䅛㌱㨲㑝     | 䅛㌱㨲㑝     | 䅛㌱㨲㑝     | 䅛㌱㨲㑝     | 䅛㌱㨲㑝     | 䅛㌱㨲㑝     | 䅛㌱㨲㑝     | 䅛㌱㨲㑝     |
|          |          | 乓        | 卆        | 乓        | ⠰⤠       | 䕌        |          |
| 噍䥄嬷㨰     | 噍䥄嬷㨰     | 噍䥄嬷㨰     | 噍䥄嬷㨰     | 噍䥄嬷㨰     | 噍䥄嬷㨰     | 噍䥄嬷㨰     | 噍䥄嬷㨰     |
| 噍䥄嬱㔺㡝    | 噍䥄嬱㔺㡝    | 噍䥄嬱㔺㡝    | 噍䥄嬱㔺㡝    | 噍䥄嬱㔺㡝    | 噍䥄嬱㔺㡝    | 噍䥄嬱㔺㡝    | 噍䥄嬱㔺㡝    |
| 噍䥄嬲㌺ㄶ    | 噍䥄嬲㌺ㄶ    | 噍䥄嬲㌺ㄶ    | 噍䥄嬲㌺ㄶ    | 噍䥄嬲㌺ㄶ    | 噍䥄嬲㌺ㄶ    | 噍䥄嬲㌺ㄶ    | 噍䥄嬲㌺ㄶ    |
| 噍䥄嬳ㄺ㈴    | 噍䥄嬳ㄺ㈴    | 噍䥄嬳ㄺ㈴    | 噍䥄嬳ㄺ㈴    | 噍䥄嬳ㄺ㈴    | 噍䥄嬳ㄺ㈴    | 噍䥄嬳ㄺ㈴    | 噍䥄嬳ㄺ㈴    |
| 䍏乔䕘呉䑛㜺そ  | 䍏乔䕘呉䑛㜺そ  | 䍏乔䕘呉䑛㜺そ  | 䍏乔䕘呉䑛㜺そ  | 䍏乔䕘呉䑛㜺そ  | 䍏乔䕘呉䑛㜺そ  | 䍏乔䕘呉䑛㜺そ  | 䍏乔䕘呉䑛㜺そ  |
| 䍏乔䕘呉䑛ㄵ㨸  | 䍏乔䕘呉䑛ㄵ㨸  | 䍏乔䕘呉䑛ㄵ㨸  | 䍏乔䕘呉䑛ㄵ㨸  | 䍏乔䕘呉䑛ㄵ㨸  | 䍏乔䕘呉䑛ㄵ㨸  | 䍏乔䕘呉䑛ㄵ㨸  | 䍏乔䕘呉䑛ㄵ㨸  |
| 䍏乔䕘呉䑛㈳㨱㙝 | 䍏乔䕘呉䑛㈳㨱㙝 | 䍏乔䕘呉䑛㈳㨱㙝 | 䍏乔䕘呉䑛㈳㨱㙝 | 䍏乔䕘呉䑛㈳㨱㙝 | 䍏乔䕘呉䑛㈳㨱㙝 | 䍏乔䕘呉䑛㈳㨱㙝 | 䍏乔䕘呉䑛㈳㨱㙝 |
| 䍏乔䕘呉䑛㌱㨲㑝 | 䍏乔䕘呉䑛㌱㨲㑝 | 䍏乔䕘呉䑛㌱㨲㑝 | 䍏乔䕘呉䑛㌱㨲㑝 | 䍏乔䕘呉䑛㌱㨲㑝 | 䍏乔䕘呉䑛㌱㨲㑝 | 䍏乔䕘呉䑛㌱㨲㑝 | 䍏乔䕘呉䑛㌱㨲㑝 |

EL

When this field is not output, the Context identifier is the same as the most recently output Context identifier.

If Context identifier tracing is disabled, then one of the following must occur:

- This field is not traced.
- This field contains a value of zero.

The encoding for this field is POD.

See Context identifier tracing.

Exception level at this address.

The encoding for this field is POD.

| EL   | Description   |
|------|---------------|
| 0b00 | EL0           |
| 0b01 | EL1           |
| 0b10 | EL2           |
| 0b11 | EL3           |

NS

Security state.

The encoding for this field is POD.

With the NSE bit, indicates the Security state associated with the address.

| NSE   | NS   | Description                                                                                      |
|-------|------|--------------------------------------------------------------------------------------------------|
| 0b0   | 0b0  | Secure state. This value is defined only if Secure state is implemented, and reserved otherwise. |
| 0b0   | 0b1  | Non-secure state.                                                                                |
| 0b1   | 0b0  | Root state. This value is defined only if FEAT_RME is implemented, and reserved otherwise.       |
| 0b1   | 0b1  | Realm state. This value is defined only if FEAT_RME is implemented, and reserved otherwise.      |

NSE

Security state, for more information see the NS field.

The encoding for this field is POD.

SF

AArch64 state.

The encoding for this field is POD.

| SF   | Description                 |
|------|-----------------------------|
| 0b0  | The PE is in AArch32 state. |
| 0b1  | The PE is in AArch64 state. |

## VMID

Virtual context identifier.

When this field is not output, the Virtual context identifier is the same as the most recently output Virtual context identifier.

If Virtual context identifier tracing is disabled, then one of the following must occur:

- This field is not traced.
- This field contains a value of zero.

The encoding for this field is POD.

See Virtual context identifier tracing.

## Element sequence

This packet encodes the following sequence:

1. Target Address element .
2. Context element .

## Additional information

For more information about the decoding of this packet see Parse\_TargetAddressPacket().

For more information about the generation of this packet see Address compression.

For more information about the encoding of this packet see Instruction set encoding.

## D5.3.66 Target Address with Context 32-bit IS1 Packet

## Purpose

Configurations

Indicates a Target Address element and a Context element .

All.

Packet Layout - Variant 1

Packet Layout - Variant 2

Figure D5-85 Target Address with Context 32-bit IS1 Packet (1)

<!-- image -->

| ⠰⤠   | 䅛㜺ㅝ   | 䅛㜺ㅝ   | 䅛㜺ㅝ   | 䅛㜺ㅝ   | 䅛㜺ㅝ   | 䅛㜺ㅝ   |
|------|-------|-------|-------|-------|-------|-------|
| 䅛ㄵ㨸  | 䅛ㄵ㨸   | 䅛ㄵ㨸   | 䅛ㄵ㨸   | 䅛ㄵ㨸   | 䅛ㄵ㨸   | 䅛ㄵ㨸   |
| 䅛㈳㨱㙝 | 䅛㈳㨱㙝  | 䅛㈳㨱㙝  | 䅛㈳㨱㙝  | 䅛㈳㨱㙝  | 䅛㈳㨱㙝  | 䅛㈳㨱㙝  |
| 䅛㌱㨲㑝 | 䅛㌱㨲㑝  | 䅛㌱㨲㑝  | 䅛㌱㨲㑝  | 䅛㌱㨲㑝  | 䅛㌱㨲㑝  | 䅛㌱㨲㑝  |
|      |       | 乓     | 卆     | 乓     | ⠰⤠    | 䕌     |

Figure D5-86 Target Address with Context 32-bit IS1 Packet (2)

<!-- image -->

## Packet Layout - Variant 3

## Packet Layout - Variant 4

## Field descriptions

A

Instruction virtual address.

Instruction virtual address bit[0] always has the value 0b0.

The address is compressed relative to address history buffer entry 0.

The encoding for this field is Bit replacement.

Context identifier.

## CONTEXTID

Figure D5-87 Target Address with Context 32-bit IS1 Packet (3)

<!-- image -->

| ⠰⤠    | 䅛㜺ㅝ   | 䅛㜺ㅝ   | 䅛㜺ㅝ   | 䅛㜺ㅝ   | 䅛㜺ㅝ   | 䅛㜺ㅝ   | 䅛㜺ㅝ   |
|-------|-------|-------|-------|-------|-------|-------|-------|
| 䅛ㄵ㨸   | 䅛ㄵ㨸   | 䅛ㄵ㨸   | 䅛ㄵ㨸   | 䅛ㄵ㨸   | 䅛ㄵ㨸   | 䅛ㄵ㨸   | 䅛ㄵ㨸   |
| 䅛㈳㨱㙝  | 䅛㈳㨱㙝  | 䅛㈳㨱㙝  | 䅛㈳㨱㙝  | 䅛㈳㨱㙝  | 䅛㈳㨱㙝  | 䅛㈳㨱㙝  | 䅛㈳㨱㙝  |
| 䅛㌱㨲㑝  | 䅛㌱㨲㑝  | 䅛㌱㨲㑝  | 䅛㌱㨲㑝  | 䅛㌱㨲㑝  | 䅛㌱㨲㑝  | 䅛㌱㨲㑝  | 䅛㌱㨲㑝  |
|       |       | 乓     | 卆     | 乓     | ⠰⤠    | 䕌     |       |
| 噍䥄嬷㨰  | 噍䥄嬷㨰  | 噍䥄嬷㨰  | 噍䥄嬷㨰  | 噍䥄嬷㨰  | 噍䥄嬷㨰  | 噍䥄嬷㨰  | 噍䥄嬷㨰  |
| 噍䥄嬱㔺㡝 | 噍䥄嬱㔺㡝 | 噍䥄嬱㔺㡝 | 噍䥄嬱㔺㡝 | 噍䥄嬱㔺㡝 | 噍䥄嬱㔺㡝 | 噍䥄嬱㔺㡝 | 噍䥄嬱㔺㡝 |
| 噍䥄嬲㌺ㄶ | 噍䥄嬲㌺ㄶ | 噍䥄嬲㌺ㄶ | 噍䥄嬲㌺ㄶ | 噍䥄嬲㌺ㄶ | 噍䥄嬲㌺ㄶ | 噍䥄嬲㌺ㄶ | 噍䥄嬲㌺ㄶ |
| 噍䥄嬳ㄺ㈴ | 噍䥄嬳ㄺ㈴ | 噍䥄嬳ㄺ㈴ | 噍䥄嬳ㄺ㈴ | 噍䥄嬳ㄺ㈴ | 噍䥄嬳ㄺ㈴ | 噍䥄嬳ㄺ㈴ | 噍䥄嬳ㄺ㈴ |

Figure D5-88 Target Address with Context 32-bit IS1 Packet (4)

<!-- image -->

| ⠰⤠       | 䅛㜺ㅝ      | 䅛㜺ㅝ      | 䅛㜺ㅝ      | 䅛㜺ㅝ      | 䅛㜺ㅝ      | 䅛㜺ㅝ      | 䅛㜺ㅝ      |
|----------|----------|----------|----------|----------|----------|----------|----------|
| 䅛ㄵ㨸      | 䅛ㄵ㨸      | 䅛ㄵ㨸      | 䅛ㄵ㨸      | 䅛ㄵ㨸      | 䅛ㄵ㨸      | 䅛ㄵ㨸      | 䅛ㄵ㨸      |
| 䅛㈳㨱㙝     | 䅛㈳㨱㙝     | 䅛㈳㨱㙝     | 䅛㈳㨱㙝     | 䅛㈳㨱㙝     | 䅛㈳㨱㙝     | 䅛㈳㨱㙝     | 䅛㈳㨱㙝     |
| 䅛㌱㨲㑝     | 䅛㌱㨲㑝     | 䅛㌱㨲㑝     | 䅛㌱㨲㑝     | 䅛㌱㨲㑝     | 䅛㌱㨲㑝     | 䅛㌱㨲㑝     | 䅛㌱㨲㑝     |
|          |          | 乓        | 卆        | 乓        | ⠰⤠       | 䕌        |          |
| 噍䥄嬷㨰     | 噍䥄嬷㨰     | 噍䥄嬷㨰     | 噍䥄嬷㨰     | 噍䥄嬷㨰     | 噍䥄嬷㨰     | 噍䥄嬷㨰     | 噍䥄嬷㨰     |
| 噍䥄嬱㔺㡝    | 噍䥄嬱㔺㡝    | 噍䥄嬱㔺㡝    | 噍䥄嬱㔺㡝    | 噍䥄嬱㔺㡝    | 噍䥄嬱㔺㡝    | 噍䥄嬱㔺㡝    | 噍䥄嬱㔺㡝    |
| 噍䥄嬲㌺ㄶ    | 噍䥄嬲㌺ㄶ    | 噍䥄嬲㌺ㄶ    | 噍䥄嬲㌺ㄶ    | 噍䥄嬲㌺ㄶ    | 噍䥄嬲㌺ㄶ    | 噍䥄嬲㌺ㄶ    | 噍䥄嬲㌺ㄶ    |
| 噍䥄嬳ㄺ㈴    | 噍䥄嬳ㄺ㈴    | 噍䥄嬳ㄺ㈴    | 噍䥄嬳ㄺ㈴    | 噍䥄嬳ㄺ㈴    | 噍䥄嬳ㄺ㈴    | 噍䥄嬳ㄺ㈴    | 噍䥄嬳ㄺ㈴    |
| 䍏乔䕘呉䑛㜺そ  | 䍏乔䕘呉䑛㜺そ  | 䍏乔䕘呉䑛㜺そ  | 䍏乔䕘呉䑛㜺そ  | 䍏乔䕘呉䑛㜺そ  | 䍏乔䕘呉䑛㜺そ  | 䍏乔䕘呉䑛㜺そ  | 䍏乔䕘呉䑛㜺そ  |
| 䍏乔䕘呉䑛ㄵ㨸  | 䍏乔䕘呉䑛ㄵ㨸  | 䍏乔䕘呉䑛ㄵ㨸  | 䍏乔䕘呉䑛ㄵ㨸  | 䍏乔䕘呉䑛ㄵ㨸  | 䍏乔䕘呉䑛ㄵ㨸  | 䍏乔䕘呉䑛ㄵ㨸  | 䍏乔䕘呉䑛ㄵ㨸  |
| 䍏乔䕘呉䑛㈳㨱㙝 | 䍏乔䕘呉䑛㈳㨱㙝 | 䍏乔䕘呉䑛㈳㨱㙝 | 䍏乔䕘呉䑛㈳㨱㙝 | 䍏乔䕘呉䑛㈳㨱㙝 | 䍏乔䕘呉䑛㈳㨱㙝 | 䍏乔䕘呉䑛㈳㨱㙝 | 䍏乔䕘呉䑛㈳㨱㙝 |
| 䍏乔䕘呉䑛㌱㨲㑝 | 䍏乔䕘呉䑛㌱㨲㑝 | 䍏乔䕘呉䑛㌱㨲㑝 | 䍏乔䕘呉䑛㌱㨲㑝 | 䍏乔䕘呉䑛㌱㨲㑝 | 䍏乔䕘呉䑛㌱㨲㑝 | 䍏乔䕘呉䑛㌱㨲㑝 | 䍏乔䕘呉䑛㌱㨲㑝 |

EL

When this field is not output, the Context identifier is the same as the most recently output Context identifier.

If Context identifier tracing is disabled, then one of the following must occur:

- This field is not traced.
- This field contains a value of zero.

The encoding for this field is POD.

See Context identifier tracing.

Exception level at this address.

The encoding for this field is POD.

| EL   | Description   |
|------|---------------|
| 0b00 | EL0           |
| 0b01 | EL1           |
| 0b10 | EL2           |
| 0b11 | EL3           |

NS

Security state.

The encoding for this field is POD.

With the NSE bit, indicates the Security state associated with the address.

| NSE   | NS   | Description                                                                                      |
|-------|------|--------------------------------------------------------------------------------------------------|
| 0b0   | 0b0  | Secure state. This value is defined only if Secure state is implemented, and reserved otherwise. |
| 0b0   | 0b1  | Non-secure state.                                                                                |
| 0b1   | 0b0  | Root state. This value is defined only if FEAT_RME is implemented, and reserved otherwise.       |
| 0b1   | 0b1  | Realm state. This value is defined only if FEAT_RME is implemented, and reserved otherwise.      |

NSE

Security state, for more information see the NS field.

The encoding for this field is POD.

SF

AArch64 state.

The encoding for this field is POD.

| SF   | Description                 |
|------|-----------------------------|
| 0b0  | The PE is in AArch32 state. |
| 0b1  | The PE is in AArch64 state. |

## VMID

Virtual context identifier.

When this field is not output, the Virtual context identifier is the same as the most recently output Virtual context identifier.

If Virtual context identifier tracing is disabled, then one of the following must occur:

- This field is not traced.
- This field contains a value of zero.

The encoding for this field is POD.

See Virtual context identifier tracing.

## Element sequence

This packet encodes the following sequence:

1. Target Address element .
2. Context element .

## Additional information

For more information about the decoding of this packet see Parse\_TargetAddressPacket().

For more information about the generation of this packet see Address compression.

For more information about the encoding of this packet see Instruction set encoding.

## D5.3.67 Target Address with Context 64-bit IS0 Packet

Purpose

Configurations

Indicates a Target Address element and a Context element .

All.

Packet Layout - Variant 1

Packet Layout - Variant 2

Figure D5-89 Target Address with Context 64-bit IS0 Packet (1)

| ⠰⤠   | 䅛㠺㉝   | 䅛㠺㉝   | 䅛㠺㉝   | 䅛㠺㉝   | 䅛㠺㉝   | 䅛㠺㉝   | 䅛㠺㉝   |
|------|-------|-------|-------|-------|-------|-------|-------|
| ⠰⤠   | 䅛ㄵ㨹   | 䅛ㄵ㨹   | 䅛ㄵ㨹   | 䅛ㄵ㨹   | 䅛ㄵ㨹   | 䅛ㄵ㨹   | 䅛ㄵ㨹   |
| 䅛㈳㨱㙝 | 䅛㈳㨱㙝  | 䅛㈳㨱㙝  | 䅛㈳㨱㙝  | 䅛㈳㨱㙝  | 䅛㈳㨱㙝  | 䅛㈳㨱㙝  | 䅛㈳㨱㙝  |
| 䅛㌱㨲㑝 | 䅛㌱㨲㑝  | 䅛㌱㨲㑝  | 䅛㌱㨲㑝  | 䅛㌱㨲㑝  | 䅛㌱㨲㑝  | 䅛㌱㨲㑝  | 䅛㌱㨲㑝  |
| 䅛㌹㨳㉝ | 䅛㌹㨳㉝  | 䅛㌹㨳㉝  | 䅛㌹㨳㉝  | 䅛㌹㨳㉝  | 䅛㌹㨳㉝  | 䅛㌹㨳㉝  | 䅛㌹㨳㉝  |
| 䅛㐷㨴そ | 䅛㐷㨴そ  | 䅛㐷㨴そ  | 䅛㐷㨴そ  | 䅛㐷㨴そ  | 䅛㐷㨴そ  | 䅛㐷㨴そ  | 䅛㐷㨴そ  |
| 䅛㔵㨴㡝 | 䅛㔵㨴㡝  | 䅛㔵㨴㡝  | 䅛㔵㨴㡝  | 䅛㔵㨴㡝  | 䅛㔵㨴㡝  | 䅛㔵㨴㡝  | 䅛㔵㨴㡝  |
| 䅛㘳㨵㙝 | 䅛㘳㨵㙝  | 䅛㘳㨵㙝  | 䅛㘳㨵㙝  | 䅛㘳㨵㙝  | 䅛㘳㨵㙝  | 䅛㘳㨵㙝  | 䅛㘳㨵㙝  |
|      |       | 乓     | 卆     | 乓     | ⠰⤠    | 䕌     |       |

Figure D5-90 Target Address with Context 64-bit IS0 Packet (2)

| ⠰⤠       | 䅛㠺㉝      | 䅛㠺㉝      | 䅛㠺㉝      | 䅛㠺㉝      | 䅛㠺㉝      | 䅛㠺㉝      | 䅛㠺㉝      |
|----------|----------|----------|----------|----------|----------|----------|----------|
| ⠰⤠       | 䅛ㄵ㨹      | 䅛ㄵ㨹      | 䅛ㄵ㨹      | 䅛ㄵ㨹      | 䅛ㄵ㨹      | 䅛ㄵ㨹      | 䅛ㄵ㨹      |
| 䅛㈳㨱㙝     | 䅛㈳㨱㙝     | 䅛㈳㨱㙝     | 䅛㈳㨱㙝     | 䅛㈳㨱㙝     | 䅛㈳㨱㙝     | 䅛㈳㨱㙝     | 䅛㈳㨱㙝     |
| 䅛㌱㨲㑝     | 䅛㌱㨲㑝     | 䅛㌱㨲㑝     | 䅛㌱㨲㑝     | 䅛㌱㨲㑝     | 䅛㌱㨲㑝     | 䅛㌱㨲㑝     | 䅛㌱㨲㑝     |
| 䅛㌹㨳㉝     | 䅛㌹㨳㉝     | 䅛㌹㨳㉝     | 䅛㌹㨳㉝     | 䅛㌹㨳㉝     | 䅛㌹㨳㉝     | 䅛㌹㨳㉝     | 䅛㌹㨳㉝     |
| 䅛㐷㨴そ     | 䅛㐷㨴そ     | 䅛㐷㨴そ     | 䅛㐷㨴そ     | 䅛㐷㨴そ     | 䅛㐷㨴そ     | 䅛㐷㨴そ     | 䅛㐷㨴そ     |
| 䅛㔵㨴㡝     | 䅛㔵㨴㡝     | 䅛㔵㨴㡝     | 䅛㔵㨴㡝     | 䅛㔵㨴㡝     | 䅛㔵㨴㡝     | 䅛㔵㨴㡝     | 䅛㔵㨴㡝     |
| 䅛㘳㨵㙝     | 䅛㘳㨵㙝     | 䅛㘳㨵㙝     | 䅛㘳㨵㙝     | 䅛㘳㨵㙝     | 䅛㘳㨵㙝     | 䅛㘳㨵㙝     | 䅛㘳㨵㙝     |
|          |          | 乓        | 卆        | 乓        | ⠰⤠       | 䕌        |          |
| 䍏乔䕘呉䑛㜺そ  | 䍏乔䕘呉䑛㜺そ  | 䍏乔䕘呉䑛㜺そ  | 䍏乔䕘呉䑛㜺そ  | 䍏乔䕘呉䑛㜺そ  | 䍏乔䕘呉䑛㜺そ  | 䍏乔䕘呉䑛㜺そ  | 䍏乔䕘呉䑛㜺そ  |
| 䍏乔䕘呉䑛ㄵ㨸  | 䍏乔䕘呉䑛ㄵ㨸  | 䍏乔䕘呉䑛ㄵ㨸  | 䍏乔䕘呉䑛ㄵ㨸  | 䍏乔䕘呉䑛ㄵ㨸  | 䍏乔䕘呉䑛ㄵ㨸  | 䍏乔䕘呉䑛ㄵ㨸  | 䍏乔䕘呉䑛ㄵ㨸  |
| 䍏乔䕘呉䑛㈳㨱㙝 | 䍏乔䕘呉䑛㈳㨱㙝 | 䍏乔䕘呉䑛㈳㨱㙝 | 䍏乔䕘呉䑛㈳㨱㙝 | 䍏乔䕘呉䑛㈳㨱㙝 | 䍏乔䕘呉䑛㈳㨱㙝 | 䍏乔䕘呉䑛㈳㨱㙝 | 䍏乔䕘呉䑛㈳㨱㙝 |
| 䍏乔䕘呉䑛㌱㨲㑝 | 䍏乔䕘呉䑛㌱㨲㑝 | 䍏乔䕘呉䑛㌱㨲㑝 | 䍏乔䕘呉䑛㌱㨲㑝 | 䍏乔䕘呉䑛㌱㨲㑝 | 䍏乔䕘呉䑛㌱㨲㑝 | 䍏乔䕘呉䑛㌱㨲㑝 | 䍏乔䕘呉䑛㌱㨲㑝 |

## Packet Layout - Variant 3

Packet Layout - Variant 4

Field descriptions

A

Figure D5-91 Target Address with Context 64-bit IS0 Packet (3)

<!-- image -->

| ⠰⤠    | 䅛㠺㉝   | 䅛㠺㉝   | 䅛㠺㉝   | 䅛㠺㉝   | 䅛㠺㉝   | 䅛㠺㉝   | 䅛㠺㉝   |
|-------|-------|-------|-------|-------|-------|-------|-------|
| ⠰⤠    | 䅛ㄵ㨹   | 䅛ㄵ㨹   | 䅛ㄵ㨹   | 䅛ㄵ㨹   | 䅛ㄵ㨹   | 䅛ㄵ㨹   | 䅛ㄵ㨹   |
| 䅛㈳㨱㙝  | 䅛㈳㨱㙝  | 䅛㈳㨱㙝  | 䅛㈳㨱㙝  | 䅛㈳㨱㙝  | 䅛㈳㨱㙝  | 䅛㈳㨱㙝  | 䅛㈳㨱㙝  |
| 䅛㌱㨲㑝  | 䅛㌱㨲㑝  | 䅛㌱㨲㑝  | 䅛㌱㨲㑝  | 䅛㌱㨲㑝  | 䅛㌱㨲㑝  | 䅛㌱㨲㑝  | 䅛㌱㨲㑝  |
| 䅛㌹㨳㉝  | 䅛㌹㨳㉝  | 䅛㌹㨳㉝  | 䅛㌹㨳㉝  | 䅛㌹㨳㉝  | 䅛㌹㨳㉝  | 䅛㌹㨳㉝  | 䅛㌹㨳㉝  |
| 䅛㐷㨴そ  | 䅛㐷㨴そ  | 䅛㐷㨴そ  | 䅛㐷㨴そ  | 䅛㐷㨴そ  | 䅛㐷㨴そ  | 䅛㐷㨴そ  | 䅛㐷㨴そ  |
| 䅛㔵㨴㡝  | 䅛㔵㨴㡝  | 䅛㔵㨴㡝  | 䅛㔵㨴㡝  | 䅛㔵㨴㡝  | 䅛㔵㨴㡝  | 䅛㔵㨴㡝  | 䅛㔵㨴㡝  |
| 䅛㘳㨵㙝  | 䅛㘳㨵㙝  | 䅛㘳㨵㙝  | 䅛㘳㨵㙝  | 䅛㘳㨵㙝  | 䅛㘳㨵㙝  | 䅛㘳㨵㙝  | 䅛㘳㨵㙝  |
|       |       | 乓     | 卆     | 乓     | ⠰⤠    | 䕌     |       |
| 噍䥄嬷㨰  | 噍䥄嬷㨰  | 噍䥄嬷㨰  | 噍䥄嬷㨰  | 噍䥄嬷㨰  | 噍䥄嬷㨰  | 噍䥄嬷㨰  | 噍䥄嬷㨰  |
| 噍䥄嬱㔺㡝 | 噍䥄嬱㔺㡝 | 噍䥄嬱㔺㡝 | 噍䥄嬱㔺㡝 | 噍䥄嬱㔺㡝 | 噍䥄嬱㔺㡝 | 噍䥄嬱㔺㡝 | 噍䥄嬱㔺㡝 |
| 噍䥄嬲㌺ㄶ | 噍䥄嬲㌺ㄶ | 噍䥄嬲㌺ㄶ | 噍䥄嬲㌺ㄶ | 噍䥄嬲㌺ㄶ | 噍䥄嬲㌺ㄶ | 噍䥄嬲㌺ㄶ | 噍䥄嬲㌺ㄶ |
| 噍䥄嬳ㄺ㈴ | 噍䥄嬳ㄺ㈴ | 噍䥄嬳ㄺ㈴ | 噍䥄嬳ㄺ㈴ | 噍䥄嬳ㄺ㈴ | 噍䥄嬳ㄺ㈴ | 噍䥄嬳ㄺ㈴ | 噍䥄嬳ㄺ㈴ |

Figure D5-92 Target Address with Context 64-bit IS0 Packet (4)

| ⠰⤠       | 䅛㠺㉝      | 䅛㠺㉝      | 䅛㠺㉝      | 䅛㠺㉝      | 䅛㠺㉝      | 䅛㠺㉝      | 䅛㠺㉝      |
|----------|----------|----------|----------|----------|----------|----------|----------|
| ⠰⤠       | 䅛ㄵ㨹      | 䅛ㄵ㨹      | 䅛ㄵ㨹      | 䅛ㄵ㨹      | 䅛ㄵ㨹      | 䅛ㄵ㨹      | 䅛ㄵ㨹      |
| 䅛㈳㨱㙝     | 䅛㈳㨱㙝     | 䅛㈳㨱㙝     | 䅛㈳㨱㙝     | 䅛㈳㨱㙝     | 䅛㈳㨱㙝     | 䅛㈳㨱㙝     | 䅛㈳㨱㙝     |
| 䅛㌱㨲㑝     | 䅛㌱㨲㑝     | 䅛㌱㨲㑝     | 䅛㌱㨲㑝     | 䅛㌱㨲㑝     | 䅛㌱㨲㑝     | 䅛㌱㨲㑝     | 䅛㌱㨲㑝     |
| 䅛㌹㨳㉝     | 䅛㌹㨳㉝     | 䅛㌹㨳㉝     | 䅛㌹㨳㉝     | 䅛㌹㨳㉝     | 䅛㌹㨳㉝     | 䅛㌹㨳㉝     | 䅛㌹㨳㉝     |
| 䅛㐷㨴そ     | 䅛㐷㨴そ     | 䅛㐷㨴そ     | 䅛㐷㨴そ     | 䅛㐷㨴そ     | 䅛㐷㨴そ     | 䅛㐷㨴そ     | 䅛㐷㨴そ     |
| 䅛㔵㨴㡝     | 䅛㔵㨴㡝     | 䅛㔵㨴㡝     | 䅛㔵㨴㡝     | 䅛㔵㨴㡝     | 䅛㔵㨴㡝     | 䅛㔵㨴㡝     | 䅛㔵㨴㡝     |
| 䅛㘳㨵㙝     | 䅛㘳㨵㙝     | 䅛㘳㨵㙝     | 䅛㘳㨵㙝     | 䅛㘳㨵㙝     | 䅛㘳㨵㙝     | 䅛㘳㨵㙝     | 䅛㘳㨵㙝     |
|          |          | 乓        | 卆        | 乓        | ⠰⤠       | 䕌        |          |
| 噍䥄嬷㨰     | 噍䥄嬷㨰     | 噍䥄嬷㨰     | 噍䥄嬷㨰     | 噍䥄嬷㨰     | 噍䥄嬷㨰     | 噍䥄嬷㨰     | 噍䥄嬷㨰     |
| 噍䥄嬱㔺㡝    | 噍䥄嬱㔺㡝    | 噍䥄嬱㔺㡝    | 噍䥄嬱㔺㡝    | 噍䥄嬱㔺㡝    | 噍䥄嬱㔺㡝    | 噍䥄嬱㔺㡝    | 噍䥄嬱㔺㡝    |
| 噍䥄嬲㌺ㄶ    | 噍䥄嬲㌺ㄶ    | 噍䥄嬲㌺ㄶ    | 噍䥄嬲㌺ㄶ    | 噍䥄嬲㌺ㄶ    | 噍䥄嬲㌺ㄶ    | 噍䥄嬲㌺ㄶ    | 噍䥄嬲㌺ㄶ    |
| 噍䥄嬳ㄺ㈴    | 噍䥄嬳ㄺ㈴    | 噍䥄嬳ㄺ㈴    | 噍䥄嬳ㄺ㈴    | 噍䥄嬳ㄺ㈴    | 噍䥄嬳ㄺ㈴    | 噍䥄嬳ㄺ㈴    | 噍䥄嬳ㄺ㈴    |
| 䍏乔䕘呉䑛㜺そ  | 䍏乔䕘呉䑛㜺そ  | 䍏乔䕘呉䑛㜺そ  | 䍏乔䕘呉䑛㜺そ  | 䍏乔䕘呉䑛㜺そ  | 䍏乔䕘呉䑛㜺そ  | 䍏乔䕘呉䑛㜺そ  | 䍏乔䕘呉䑛㜺そ  |
| 䍏乔䕘呉䑛ㄵ㨸  | 䍏乔䕘呉䑛ㄵ㨸  | 䍏乔䕘呉䑛ㄵ㨸  | 䍏乔䕘呉䑛ㄵ㨸  | 䍏乔䕘呉䑛ㄵ㨸  | 䍏乔䕘呉䑛ㄵ㨸  | 䍏乔䕘呉䑛ㄵ㨸  | 䍏乔䕘呉䑛ㄵ㨸  |
| 䍏乔䕘呉䑛㈳㨱㙝 | 䍏乔䕘呉䑛㈳㨱㙝 | 䍏乔䕘呉䑛㈳㨱㙝 | 䍏乔䕘呉䑛㈳㨱㙝 | 䍏乔䕘呉䑛㈳㨱㙝 | 䍏乔䕘呉䑛㈳㨱㙝 | 䍏乔䕘呉䑛㈳㨱㙝 | 䍏乔䕘呉䑛㈳㨱㙝 |
| 䍏乔䕘呉䑛㌱㨲㑝 | 䍏乔䕘呉䑛㌱㨲㑝 | 䍏乔䕘呉䑛㌱㨲㑝 | 䍏乔䕘呉䑛㌱㨲㑝 | 䍏乔䕘呉䑛㌱㨲㑝 | 䍏乔䕘呉䑛㌱㨲㑝 | 䍏乔䕘呉䑛㌱㨲㑝 | 䍏乔䕘呉䑛㌱㨲㑝 |

## CONTEXTID

EL

Instruction virtual address.

Instruction virtual address bits[1:0] always have the value 0b00.

The address is compressed relative to address history buffer entry 0.

The encoding for this field is Bit replacement.

Context identifier.

When this field is not output, the Context identifier is the same as the most recently output Context identifier.

If Context identifier tracing is disabled, then one of the following must occur:

- This field is not traced.
- This field contains a value of zero.

The encoding for this field is POD.

See Context identifier tracing.

Exception level at this address.

The encoding for this field is POD.

| EL   | Description   |
|------|---------------|
| 0b00 | EL0           |
| 0b01 | EL1           |
| 0b10 | EL2           |
| 0b11 | EL3           |

NS

Security state.

The encoding for this field is POD.

With the NSE bit, indicates the Security state associated with the address.

| NSE   | NS   | Description                                                                                      |
|-------|------|--------------------------------------------------------------------------------------------------|
| 0b0   | 0b0  | Secure state. This value is defined only if Secure state is implemented, and reserved otherwise. |
| 0b0   | 0b1  | Non-secure state.                                                                                |
| 0b1   | 0b0  | Root state. This value is defined only if FEAT_RME is implemented, and reserved otherwise.       |
| 0b1   | 0b1  | Realm state. This value is defined only if FEAT_RME is implemented, and reserved otherwise.      |

NSE

Security state, for more information see the NS field.

The encoding for this field is POD.

SF

AArch64 state.

The encoding for this field is POD.

| SF   | Description                 |
|------|-----------------------------|
| 0b0  | The PE is in AArch32 state. |
| 0b1  | The PE is in AArch64 state. |

## VMID

Virtual context identifier.

When this field is not output, the Virtual context identifier is the same as the most recently output Virtual context identifier.

If Virtual context identifier tracing is disabled, then one of the following must occur:

- This field is not traced.
- This field contains a value of zero.

The encoding for this field is POD.

See Virtual context identifier tracing.

## Element sequence

This packet encodes the following sequence:

1. Target Address element .
2. Context element .

## Additional information

For more information about the decoding of this packet see Parse\_TargetAddressPacket().

For more information about the generation of this packet see Address compression.

For more information about the encoding of this packet see Instruction set encoding.

## D5.3.68 Target Address with Context 64-bit IS1 Packet

Purpose

Configurations

Indicates a Target Address element and a Context element .

All.

Packet Layout - Variant 1

Packet Layout - Variant 2

Figure D5-93 Target Address with Context 64-bit IS1 Packet (1)

| ⠰⤠   | 䅛㜺ㅝ   | 䅛㜺ㅝ   | 䅛㜺ㅝ   | 䅛㜺ㅝ   | 䅛㜺ㅝ   | 䅛㜺ㅝ   | 䅛㜺ㅝ   |
|------|-------|-------|-------|-------|-------|-------|-------|
| 䅛ㄵ㨸  | 䅛ㄵ㨸   | 䅛ㄵ㨸   | 䅛ㄵ㨸   | 䅛ㄵ㨸   | 䅛ㄵ㨸   | 䅛ㄵ㨸   | 䅛ㄵ㨸   |
| 䅛㈳㨱㙝 | 䅛㈳㨱㙝  | 䅛㈳㨱㙝  | 䅛㈳㨱㙝  | 䅛㈳㨱㙝  | 䅛㈳㨱㙝  | 䅛㈳㨱㙝  | 䅛㈳㨱㙝  |
| 䅛㌱㨲㑝 | 䅛㌱㨲㑝  | 䅛㌱㨲㑝  | 䅛㌱㨲㑝  | 䅛㌱㨲㑝  | 䅛㌱㨲㑝  | 䅛㌱㨲㑝  | 䅛㌱㨲㑝  |
| 䅛㌹㨳㉝ | 䅛㌹㨳㉝  | 䅛㌹㨳㉝  | 䅛㌹㨳㉝  | 䅛㌹㨳㉝  | 䅛㌹㨳㉝  | 䅛㌹㨳㉝  | 䅛㌹㨳㉝  |
| 䅛㐷㨴そ | 䅛㐷㨴そ  | 䅛㐷㨴そ  | 䅛㐷㨴そ  | 䅛㐷㨴そ  | 䅛㐷㨴そ  | 䅛㐷㨴そ  | 䅛㐷㨴そ  |
| 䅛㔵㨴㡝 | 䅛㔵㨴㡝  | 䅛㔵㨴㡝  | 䅛㔵㨴㡝  | 䅛㔵㨴㡝  | 䅛㔵㨴㡝  | 䅛㔵㨴㡝  | 䅛㔵㨴㡝  |
| 䅛㘳㨵㙝 | 䅛㘳㨵㙝  | 䅛㘳㨵㙝  | 䅛㘳㨵㙝  | 䅛㘳㨵㙝  | 䅛㘳㨵㙝  | 䅛㘳㨵㙝  | 䅛㘳㨵㙝  |
|      |       | 乓     | 卆     | 乓     | ⠰⤠    | 䕌     |       |

Figure D5-94 Target Address with Context 64-bit IS1 Packet (2)

| ⠰⤠       | 䅛㜺ㅝ      | 䅛㜺ㅝ      | 䅛㜺ㅝ      | 䅛㜺ㅝ      | 䅛㜺ㅝ      | 䅛㜺ㅝ      | 䅛㜺ㅝ      |
|----------|----------|----------|----------|----------|----------|----------|----------|
| 䅛ㄵ㨸      | 䅛ㄵ㨸      | 䅛ㄵ㨸      | 䅛ㄵ㨸      | 䅛ㄵ㨸      | 䅛ㄵ㨸      | 䅛ㄵ㨸      | 䅛ㄵ㨸      |
| 䅛㈳㨱㙝     | 䅛㈳㨱㙝     | 䅛㈳㨱㙝     | 䅛㈳㨱㙝     | 䅛㈳㨱㙝     | 䅛㈳㨱㙝     | 䅛㈳㨱㙝     | 䅛㈳㨱㙝     |
| 䅛㌱㨲㑝     | 䅛㌱㨲㑝     | 䅛㌱㨲㑝     | 䅛㌱㨲㑝     | 䅛㌱㨲㑝     | 䅛㌱㨲㑝     | 䅛㌱㨲㑝     | 䅛㌱㨲㑝     |
| 䅛㌹㨳㉝     | 䅛㌹㨳㉝     | 䅛㌹㨳㉝     | 䅛㌹㨳㉝     | 䅛㌹㨳㉝     | 䅛㌹㨳㉝     | 䅛㌹㨳㉝     | 䅛㌹㨳㉝     |
| 䅛㐷㨴そ     | 䅛㐷㨴そ     | 䅛㐷㨴そ     | 䅛㐷㨴そ     | 䅛㐷㨴そ     | 䅛㐷㨴そ     | 䅛㐷㨴そ     | 䅛㐷㨴そ     |
| 䅛㔵㨴㡝     | 䅛㔵㨴㡝     | 䅛㔵㨴㡝     | 䅛㔵㨴㡝     | 䅛㔵㨴㡝     | 䅛㔵㨴㡝     | 䅛㔵㨴㡝     | 䅛㔵㨴㡝     |
| 䅛㘳㨵㙝     | 䅛㘳㨵㙝     | 䅛㘳㨵㙝     | 䅛㘳㨵㙝     | 䅛㘳㨵㙝     | 䅛㘳㨵㙝     | 䅛㘳㨵㙝     | 䅛㘳㨵㙝     |
|          |          | 乓        | 卆        | 乓        | ⠰⤠       | 䕌        |          |
| 䍏乔䕘呉䑛㜺そ  | 䍏乔䕘呉䑛㜺そ  | 䍏乔䕘呉䑛㜺そ  | 䍏乔䕘呉䑛㜺そ  | 䍏乔䕘呉䑛㜺そ  | 䍏乔䕘呉䑛㜺そ  | 䍏乔䕘呉䑛㜺そ  | 䍏乔䕘呉䑛㜺そ  |
| 䍏乔䕘呉䑛ㄵ㨸  | 䍏乔䕘呉䑛ㄵ㨸  | 䍏乔䕘呉䑛ㄵ㨸  | 䍏乔䕘呉䑛ㄵ㨸  | 䍏乔䕘呉䑛ㄵ㨸  | 䍏乔䕘呉䑛ㄵ㨸  | 䍏乔䕘呉䑛ㄵ㨸  | 䍏乔䕘呉䑛ㄵ㨸  |
| 䍏乔䕘呉䑛㈳㨱㙝 | 䍏乔䕘呉䑛㈳㨱㙝 | 䍏乔䕘呉䑛㈳㨱㙝 | 䍏乔䕘呉䑛㈳㨱㙝 | 䍏乔䕘呉䑛㈳㨱㙝 | 䍏乔䕘呉䑛㈳㨱㙝 | 䍏乔䕘呉䑛㈳㨱㙝 | 䍏乔䕘呉䑛㈳㨱㙝 |
| 䍏乔䕘呉䑛㌱㨲㑝 | 䍏乔䕘呉䑛㌱㨲㑝 | 䍏乔䕘呉䑛㌱㨲㑝 | 䍏乔䕘呉䑛㌱㨲㑝 | 䍏乔䕘呉䑛㌱㨲㑝 | 䍏乔䕘呉䑛㌱㨲㑝 | 䍏乔䕘呉䑛㌱㨲㑝 | 䍏乔䕘呉䑛㌱㨲㑝 |

## Packet Layout - Variant 3

Packet Layout - Variant 4

Field descriptions

A

Figure D5-95 Target Address with Context 64-bit IS1 Packet (3)

<!-- image -->

| ⠰⤠    | 䅛㜺ㅝ   | 䅛㜺ㅝ   | 䅛㜺ㅝ   | 䅛㜺ㅝ   | 䅛㜺ㅝ   | 䅛㜺ㅝ   | 䅛㜺ㅝ   |
|-------|-------|-------|-------|-------|-------|-------|-------|
| 䅛ㄵ㨸   | 䅛ㄵ㨸   | 䅛ㄵ㨸   | 䅛ㄵ㨸   | 䅛ㄵ㨸   | 䅛ㄵ㨸   | 䅛ㄵ㨸   | 䅛ㄵ㨸   |
| 䅛㈳㨱㙝  | 䅛㈳㨱㙝  | 䅛㈳㨱㙝  | 䅛㈳㨱㙝  | 䅛㈳㨱㙝  | 䅛㈳㨱㙝  | 䅛㈳㨱㙝  | 䅛㈳㨱㙝  |
| 䅛㌱㨲㑝  | 䅛㌱㨲㑝  | 䅛㌱㨲㑝  | 䅛㌱㨲㑝  | 䅛㌱㨲㑝  | 䅛㌱㨲㑝  | 䅛㌱㨲㑝  | 䅛㌱㨲㑝  |
| 䅛㌹㨳㉝  | 䅛㌹㨳㉝  | 䅛㌹㨳㉝  | 䅛㌹㨳㉝  | 䅛㌹㨳㉝  | 䅛㌹㨳㉝  | 䅛㌹㨳㉝  | 䅛㌹㨳㉝  |
| 䅛㐷㨴そ  | 䅛㐷㨴そ  | 䅛㐷㨴そ  | 䅛㐷㨴そ  | 䅛㐷㨴そ  | 䅛㐷㨴そ  | 䅛㐷㨴そ  | 䅛㐷㨴そ  |
| 䅛㔵㨴㡝  | 䅛㔵㨴㡝  | 䅛㔵㨴㡝  | 䅛㔵㨴㡝  | 䅛㔵㨴㡝  | 䅛㔵㨴㡝  | 䅛㔵㨴㡝  | 䅛㔵㨴㡝  |
| 䅛㘳㨵㙝  | 䅛㘳㨵㙝  | 䅛㘳㨵㙝  | 䅛㘳㨵㙝  | 䅛㘳㨵㙝  | 䅛㘳㨵㙝  | 䅛㘳㨵㙝  | 䅛㘳㨵㙝  |
|       |       | 乓     | 卆     | 乓     | ⠰⤠    | 䕌     |       |
| 噍䥄嬷㨰  | 噍䥄嬷㨰  | 噍䥄嬷㨰  | 噍䥄嬷㨰  | 噍䥄嬷㨰  | 噍䥄嬷㨰  | 噍䥄嬷㨰  | 噍䥄嬷㨰  |
| 噍䥄嬱㔺㡝 | 噍䥄嬱㔺㡝 | 噍䥄嬱㔺㡝 | 噍䥄嬱㔺㡝 | 噍䥄嬱㔺㡝 | 噍䥄嬱㔺㡝 | 噍䥄嬱㔺㡝 | 噍䥄嬱㔺㡝 |
| 噍䥄嬲㌺ㄶ | 噍䥄嬲㌺ㄶ | 噍䥄嬲㌺ㄶ | 噍䥄嬲㌺ㄶ | 噍䥄嬲㌺ㄶ | 噍䥄嬲㌺ㄶ | 噍䥄嬲㌺ㄶ | 噍䥄嬲㌺ㄶ |
| 噍䥄嬳ㄺ㈴ | 噍䥄嬳ㄺ㈴ | 噍䥄嬳ㄺ㈴ | 噍䥄嬳ㄺ㈴ | 噍䥄嬳ㄺ㈴ | 噍䥄嬳ㄺ㈴ | 噍䥄嬳ㄺ㈴ | 噍䥄嬳ㄺ㈴ |

Figure D5-96 Target Address with Context 64-bit IS1 Packet (4)

| ⠰⤠       | 䅛㜺ㅝ      | 䅛㜺ㅝ      | 䅛㜺ㅝ      | 䅛㜺ㅝ      | 䅛㜺ㅝ      | 䅛㜺ㅝ      | 䅛㜺ㅝ      |
|----------|----------|----------|----------|----------|----------|----------|----------|
| 䅛ㄵ㨸      | 䅛ㄵ㨸      | 䅛ㄵ㨸      | 䅛ㄵ㨸      | 䅛ㄵ㨸      | 䅛ㄵ㨸      | 䅛ㄵ㨸      | 䅛ㄵ㨸      |
| 䅛㈳㨱㙝     | 䅛㈳㨱㙝     | 䅛㈳㨱㙝     | 䅛㈳㨱㙝     | 䅛㈳㨱㙝     | 䅛㈳㨱㙝     | 䅛㈳㨱㙝     | 䅛㈳㨱㙝     |
| 䅛㌱㨲㑝     | 䅛㌱㨲㑝     | 䅛㌱㨲㑝     | 䅛㌱㨲㑝     | 䅛㌱㨲㑝     | 䅛㌱㨲㑝     | 䅛㌱㨲㑝     | 䅛㌱㨲㑝     |
| 䅛㌹㨳㉝     | 䅛㌹㨳㉝     | 䅛㌹㨳㉝     | 䅛㌹㨳㉝     | 䅛㌹㨳㉝     | 䅛㌹㨳㉝     | 䅛㌹㨳㉝     | 䅛㌹㨳㉝     |
| 䅛㐷㨴そ     | 䅛㐷㨴そ     | 䅛㐷㨴そ     | 䅛㐷㨴そ     | 䅛㐷㨴そ     | 䅛㐷㨴そ     | 䅛㐷㨴そ     | 䅛㐷㨴そ     |
| 䅛㔵㨴㡝     | 䅛㔵㨴㡝     | 䅛㔵㨴㡝     | 䅛㔵㨴㡝     | 䅛㔵㨴㡝     | 䅛㔵㨴㡝     | 䅛㔵㨴㡝     | 䅛㔵㨴㡝     |
| 䅛㘳㨵㙝     | 䅛㘳㨵㙝     | 䅛㘳㨵㙝     | 䅛㘳㨵㙝     | 䅛㘳㨵㙝     | 䅛㘳㨵㙝     | 䅛㘳㨵㙝     | 䅛㘳㨵㙝     |
|          |          | 乓        | 卆        | 乓        | ⠰⤠       | 䕌        |          |
| 噍䥄嬷㨰     | 噍䥄嬷㨰     | 噍䥄嬷㨰     | 噍䥄嬷㨰     | 噍䥄嬷㨰     | 噍䥄嬷㨰     | 噍䥄嬷㨰     | 噍䥄嬷㨰     |
| 噍䥄嬱㔺㡝    | 噍䥄嬱㔺㡝    | 噍䥄嬱㔺㡝    | 噍䥄嬱㔺㡝    | 噍䥄嬱㔺㡝    | 噍䥄嬱㔺㡝    | 噍䥄嬱㔺㡝    | 噍䥄嬱㔺㡝    |
| 噍䥄嬲㌺ㄶ    | 噍䥄嬲㌺ㄶ    | 噍䥄嬲㌺ㄶ    | 噍䥄嬲㌺ㄶ    | 噍䥄嬲㌺ㄶ    | 噍䥄嬲㌺ㄶ    | 噍䥄嬲㌺ㄶ    | 噍䥄嬲㌺ㄶ    |
| 噍䥄嬳ㄺ㈴    | 噍䥄嬳ㄺ㈴    | 噍䥄嬳ㄺ㈴    | 噍䥄嬳ㄺ㈴    | 噍䥄嬳ㄺ㈴    | 噍䥄嬳ㄺ㈴    | 噍䥄嬳ㄺ㈴    | 噍䥄嬳ㄺ㈴    |
| 䍏乔䕘呉䑛㜺そ  | 䍏乔䕘呉䑛㜺そ  | 䍏乔䕘呉䑛㜺そ  | 䍏乔䕘呉䑛㜺そ  | 䍏乔䕘呉䑛㜺そ  | 䍏乔䕘呉䑛㜺そ  | 䍏乔䕘呉䑛㜺そ  | 䍏乔䕘呉䑛㜺そ  |
| 䍏乔䕘呉䑛ㄵ㨸  | 䍏乔䕘呉䑛ㄵ㨸  | 䍏乔䕘呉䑛ㄵ㨸  | 䍏乔䕘呉䑛ㄵ㨸  | 䍏乔䕘呉䑛ㄵ㨸  | 䍏乔䕘呉䑛ㄵ㨸  | 䍏乔䕘呉䑛ㄵ㨸  | 䍏乔䕘呉䑛ㄵ㨸  |
| 䍏乔䕘呉䑛㈳㨱㙝 | 䍏乔䕘呉䑛㈳㨱㙝 | 䍏乔䕘呉䑛㈳㨱㙝 | 䍏乔䕘呉䑛㈳㨱㙝 | 䍏乔䕘呉䑛㈳㨱㙝 | 䍏乔䕘呉䑛㈳㨱㙝 | 䍏乔䕘呉䑛㈳㨱㙝 | 䍏乔䕘呉䑛㈳㨱㙝 |
| 䍏乔䕘呉䑛㌱㨲㑝 | 䍏乔䕘呉䑛㌱㨲㑝 | 䍏乔䕘呉䑛㌱㨲㑝 | 䍏乔䕘呉䑛㌱㨲㑝 | 䍏乔䕘呉䑛㌱㨲㑝 | 䍏乔䕘呉䑛㌱㨲㑝 | 䍏乔䕘呉䑛㌱㨲㑝 | 䍏乔䕘呉䑛㌱㨲㑝 |

## CONTEXTID

EL

Instruction virtual address.

Instruction virtual address bit[0] always has the value 0b0.

The address is compressed relative to address history buffer entry 0.

The encoding for this field is Bit replacement.

Context identifier.

When this field is not output, the Context identifier is the same as the most recently output Context identifier.

If Context identifier tracing is disabled, then one of the following must occur:

- This field is not traced.
- This field contains a value of zero.

The encoding for this field is POD.

See Context identifier tracing.

Exception level at this address.

The encoding for this field is POD.

| EL   | Description   |
|------|---------------|
| 0b00 | EL0           |
| 0b01 | EL1           |
| 0b10 | EL2           |
| 0b11 | EL3           |

NS

Security state.

The encoding for this field is POD.

With the NSE bit, indicates the Security state associated with the address.

| NSE   | NS   | Description                                                                                      |
|-------|------|--------------------------------------------------------------------------------------------------|
| 0b0   | 0b0  | Secure state. This value is defined only if Secure state is implemented, and reserved otherwise. |
| 0b0   | 0b1  | Non-secure state.                                                                                |
| 0b1   | 0b0  | Root state. This value is defined only if FEAT_RME is implemented, and reserved otherwise.       |
| 0b1   | 0b1  | Realm state. This value is defined only if FEAT_RME is implemented, and reserved otherwise.      |

NSE

Security state, for more information see the NS field.

The encoding for this field is POD.

SF

AArch64 state.

The encoding for this field is POD.

| SF   | Description                 |
|------|-----------------------------|
| 0b0  | The PE is in AArch32 state. |
| 0b1  | The PE is in AArch64 state. |

## VMID

Virtual context identifier.

When this field is not output, the Virtual context identifier is the same as the most recently output Virtual context identifier.

If Virtual context identifier tracing is disabled, then one of the following must occur:

- This field is not traced.
- This field contains a value of zero.

The encoding for this field is POD.

See Virtual context identifier tracing.

## Element sequence

This packet encodes the following sequence:

1. Target Address element .
2. Context element .

## Additional information

For more information about the decoding of this packet see Parse\_TargetAddressPacket().

For more information about the generation of this packet see Address compression.

For more information about the encoding of this packet see Instruction set encoding.

## D5.3.69 Trace Info Packet

## Purpose

## Configurations

Resets trace compression to a known architectural state.

All.

The trace info packet resets the trace compression to a known state.

Any fields which are not output are treated as if the value is zero.

## Packet Layout - Variant 1

## Packet Layout - Variant 2

## Packet Layout - Variant 3

<!-- image -->

Figure D5-97 Trace Info Packet (1)

Figure D5-98 Trace Info Packet (2)

<!-- image -->

Figure D5-99 Trace Info Packet (3)

<!-- image -->

| 䌰        | 卐䕃嬶㨰     | 卐䕃嬶㨰     | 卐䕃嬶㨰     | 卐䕃嬶㨰   | 卐䕃嬶㨰   | 卐䕃嬶㨰   | 卐䕃嬶㨰   |
|----------|----------|----------|----------|--------|--------|--------|--------|
| 䌰        | 卐䕃嬱㌺㝝    | 卐䕃嬱㌺㝝    | 卐䕃嬱㌺㝝    | 卐䕃嬱㌺㝝  | 卐䕃嬱㌺㝝  | 卐䕃嬱㌺㝝  | 卐䕃嬱㌺㝝  |
| 䌰        | 卐䕃嬲〺ㄴ    | 卐䕃嬲〺ㄴ    | 卐䕃嬲〺ㄴ    | 卐䕃嬲〺ㄴ  | 卐䕃嬲〺ㄴ  | 卐䕃嬲〺ㄴ  | 卐䕃嬲〺ㄴ  |
| 䌰        | 卐䕃嬲㜺㈱    | 卐䕃嬲㜺㈱    | 卐䕃嬲㜺㈱    | 卐䕃嬲㜺㈱  | 卐䕃嬲㜺㈱  | 卐䕃嬲㜺㈱  | 卐䕃嬲㜺㈱  |
| ⠰⤠⠰⤠⠰⤠⠰⤠ | ⠰⤠⠰⤠⠰⤠⠰⤠ | ⠰⤠⠰⤠⠰⤠⠰⤠ | ⠰⤠⠰⤠⠰⤠⠰⤠ | 卐䕃嬳ㄺ㈸  | 卐䕃嬳ㄺ㈸  |        |        |

## Packet Layout - Variant 4

## Packet Layout - Variant 5

## Packet Layout - Variant 6

<!-- image -->

| ⠰⤠       |          | ⠰⤠⠰⤠⠰⤠⠰⤠⠰⤠   | ⠰⤠⠰⤠⠰⤠⠰⤠⠰⤠   | ⠰⤠⠰⤠⠰⤠⠰⤠⠰⤠   | ⠰⤠⠰⤠⠰⤠⠰⤠⠰⤠   | ⠰⤠⠰⤠⠰⤠⠰⤠⠰⤠   |       |
|----------|----------|--------------|--------------|--------------|--------------|--------------|-------|
| 䌰        | 卐䕃嬶㨰     | 卐䕃嬶㨰         | 卐䕃嬶㨰         | 卐䕃嬶㨰         | 卐䕃嬶㨰         | 卐䕃嬶㨰         | 卐䕃嬶㨰  |
| 䌰        | 卐䕃嬱㌺㝝    | 卐䕃嬱㌺㝝        | 卐䕃嬱㌺㝝        | 卐䕃嬱㌺㝝        | 卐䕃嬱㌺㝝        | 卐䕃嬱㌺㝝        | 卐䕃嬱㌺㝝 |
| 䌰        | 卐䕃嬲〺ㄴ    | 卐䕃嬲〺ㄴ        | 卐䕃嬲〺ㄴ        | 卐䕃嬲〺ㄴ        | 卐䕃嬲〺ㄴ        | 卐䕃嬲〺ㄴ        | 卐䕃嬲〺ㄴ |
| 䌰        | 卐䕃嬲㜺㈱    | 卐䕃嬲㜺㈱        | 卐䕃嬲㜺㈱        | 卐䕃嬲㜺㈱        | 卐䕃嬲㜺㈱        | 卐䕃嬲㜺㈱        | 卐䕃嬲㜺㈱ |
| ⠰⤠⠰⤠⠰⤠⠰⤠ | ⠰⤠⠰⤠⠰⤠⠰⤠ | ⠰⤠⠰⤠⠰⤠⠰⤠     | ⠰⤠⠰⤠⠰⤠⠰⤠     | 卐䕃嬳ㄺ㈸        | 卐䕃嬳ㄺ㈸        | 卐䕃嬳ㄺ㈸        |       |

Figure D5-100 Trace Info Packet (4)

Figure D5-101 Trace Info Packet (5)

<!-- image -->

Figure D5-102 Trace Info Packet (6)

<!-- image -->

## Packet Layout - Variant 7

## Packet Layout - Variant 8

Field descriptions

C0

Continuation Bit.

The encoding for this field is Unary code.

| C0   | Description                                     |
|------|-------------------------------------------------|
| 0b0  | Last byte in this section.                      |
| 0b1  | At least one more byte follows in this section. |

C1

Continuation Bit.

The encoding for this field is Unary code.

| 䌰        | 卐䕃嬶㨰     | 卐䕃嬶㨰     | 卐䕃嬶㨰     | 卐䕃嬶㨰   | 卐䕃嬶㨰   | 卐䕃嬶㨰   |
|----------|----------|----------|----------|--------|--------|--------|
| 䌰        | 卐䕃嬱㌺㝝    | 卐䕃嬱㌺㝝    | 卐䕃嬱㌺㝝    | 卐䕃嬱㌺㝝  | 卐䕃嬱㌺㝝  | 卐䕃嬱㌺㝝  |
| 䌰        | 卐䕃嬲〺ㄴ    | 卐䕃嬲〺ㄴ    | 卐䕃嬲〺ㄴ    | 卐䕃嬲〺ㄴ  | 卐䕃嬲〺ㄴ  | 卐䕃嬲〺ㄴ  |
| 䌰        | 卐䕃嬲㜺㈱    | 卐䕃嬲㜺㈱    | 卐䕃嬲㜺㈱    | 卐䕃嬲㜺㈱  | 卐䕃嬲㜺㈱  | 卐䕃嬲㜺㈱  |
| ⠰⤠⠰⤠⠰⤠⠰⤠ | ⠰⤠⠰⤠⠰⤠⠰⤠ | ⠰⤠⠰⤠⠰⤠⠰⤠ | ⠰⤠⠰⤠⠰⤠⠰⤠ | 卐䕃嬳ㄺ㈸  | 卐䕃嬳ㄺ㈸  |        |
| 䌱        | 䍙䍔嬶㨰     | 䍙䍔嬶㨰     | 䍙䍔嬶㨰     | 䍙䍔嬶㨰   | 䍙䍔嬶㨰   | 䍙䍔嬶㨰   |
| ⠰⤠⠰⤠⠰⤠   | ⠰⤠⠰⤠⠰⤠   | ⠰⤠⠰⤠⠰⤠   | 䍙䍔嬱ㄺ㝝    | 䍙䍔嬱ㄺ㝝  | 䍙䍔嬱ㄺ㝝  |        |

## Figure D5-103 Trace Info Packet (7)

<!-- image -->

| ⠰⤠       |          | ⠰⤠⠰⤠⠰⤠⠰⤠⠰⤠   | ⠰⤠⠰⤠⠰⤠⠰⤠⠰⤠   | ⠰⤠⠰⤠⠰⤠⠰⤠⠰⤠   | ⠰⤠⠰⤠⠰⤠⠰⤠⠰⤠   | ⠰⤠⠰⤠⠰⤠⠰⤠⠰⤠   |       |
|----------|----------|--------------|--------------|--------------|--------------|--------------|-------|
| 䌰        | 卐䕃嬶㨰     | 卐䕃嬶㨰         | 卐䕃嬶㨰         | 卐䕃嬶㨰         | 卐䕃嬶㨰         | 卐䕃嬶㨰         | 卐䕃嬶㨰  |
| 䌰        | 卐䕃嬱㌺㝝    | 卐䕃嬱㌺㝝        | 卐䕃嬱㌺㝝        | 卐䕃嬱㌺㝝        | 卐䕃嬱㌺㝝        | 卐䕃嬱㌺㝝        | 卐䕃嬱㌺㝝 |
| 䌰        | 卐䕃嬲〺ㄴ    | 卐䕃嬲〺ㄴ        | 卐䕃嬲〺ㄴ        | 卐䕃嬲〺ㄴ        | 卐䕃嬲〺ㄴ        | 卐䕃嬲〺ㄴ        | 卐䕃嬲〺ㄴ |
| 䌰        | 卐䕃嬲㜺㈱    | 卐䕃嬲㜺㈱        | 卐䕃嬲㜺㈱        | 卐䕃嬲㜺㈱        | 卐䕃嬲㜺㈱        | 卐䕃嬲㜺㈱        | 卐䕃嬲㜺㈱ |
| ⠰⤠⠰⤠⠰⤠⠰⤠ | ⠰⤠⠰⤠⠰⤠⠰⤠ | ⠰⤠⠰⤠⠰⤠⠰⤠     | ⠰⤠⠰⤠⠰⤠⠰⤠     | 卐䕃嬳ㄺ㈸        | 卐䕃嬳ㄺ㈸        | 卐䕃嬳ㄺ㈸        | 卐䕃嬳ㄺ㈸ |
| 䌱        | 䍙䍔嬶㨰     | 䍙䍔嬶㨰         | 䍙䍔嬶㨰         | 䍙䍔嬶㨰         | 䍙䍔嬶㨰         | 䍙䍔嬶㨰         | 䍙䍔嬶㨰  |
| ⠰⤠⠰⤠⠰⤠   | ⠰⤠⠰⤠⠰⤠   | ⠰⤠⠰⤠⠰⤠       | 䍙䍔嬱ㄺ㝝        | 䍙䍔嬱ㄺ㝝        | 䍙䍔嬱ㄺ㝝        | 䍙䍔嬱ㄺ㝝        | 䍙䍔嬱ㄺ㝝 |

## Figure D5-104 Trace Info Packet (8)

| C1   | Description                                     |
|------|-------------------------------------------------|
| 0b0  | Last byte in this section.                      |
| 0b1  | At least one more byte follows in this section. |

CC

Cycle count enable indicator.

When this field is not output, it is treated as if it is zero.

The encoding for this field is POD.

| CC   | Description                    |
|------|--------------------------------|
| 0b0  | Cycle counting is not enabled. |
| 0b1  | Cycle counting is enabled.     |

| CYCT   | The cycle count threshold. When this field is not output, it is treated as if it is zero. The encoding for this field is unsigned LE128n.   |
|--------|---------------------------------------------------------------------------------------------------------------------------------------------|
| SPEC   | The number of uncommitted P0 elements in the trace. When this field is not output, it is treated as if it is zero.                          |

| T   | Description                                               |
|-----|-----------------------------------------------------------|
| 0b0 | The PE is not currently executing in Transactional state. |
| 0b1 | The PE is currently executing in Transactional state.     |

## Element sequence

This packet encodes the following sequence:

1. Trace Info element .

## Additional information

For more information about the decoding of this packet see TraceInfoPacket().

## D5.3.70 Trace On Packet

## Purpose

## Configurations

Indicates that there has been a discontinuity in the trace element stream.

All.

ATrace On packet indicates to a trace analyzer that the trace unit has generated a Trace On element .

## Packet Layout

## Element sequence

This packet encodes the following sequence:

1. Trace On element .

## Additional information

For more information about the decoding of this packet see TraceOnPacket().

Figure D5-105 Trace On Packet

<!-- image -->

## D5.3.71 Transaction Commit Packet

## Purpose

Indicates that the PE has successfully finished an outer transaction and is leaving Transactional state.

All.

Packet Layout

## Element sequence

This packet encodes the following sequence:

1. Transaction Commit element .

## Additional information

For more information about the decoding of this packet see TransactionCommitPacket().

Configurations

Figure D5-106 Transaction Commit Packet

<!-- image -->

## D5.3.72 Transaction Start Packet

## Purpose

Indicates that the PE has started to execute in Transactional state.

All.

Packet Layout

## Element sequence

This packet encodes the following sequence:

1. Transaction Start element .

## Additional information

For more information about the decoding of this packet see TransactionStartPacket().

Configurations

Figure D5-107 Transaction Start Packet

<!-- image -->

## D5.3.73 Transaction Failure Packet

## Purpose

Indicates that a Transaction Failure has occurred.

All.

## Packet Layout

## Field descriptions

E

Identifies the elements that are indicated by this packet.

The encoding for this field is POD.

| E    | Description                          |
|------|--------------------------------------|
| 0b01 | 1. Transaction Failure element .     |
| 0b10 | 1. Target Address element (UNKNOWN). |
|      | 2. Transaction Failure element .     |

All other values are reserved. Reserved values might be defined in a future version of the architecture.

## Additional information

For more information about the decoding of this packet see Parse\_ExceptionPacket().

For more information about the generation of this packet see Address compression.

Configurations

Figure D5-108 Transaction Failure Packet

<!-- image -->

| 䕛ㅝ   | 䕛そ   |
|------|------|

## Chapter D6 The Trace Buffer Extension

This chapter describes the Trace Buffer Extension (TRBE). It contains the following sections:

- About the Trace Buffer Extension.
- The trace buffer.
- Trace buffer Self-hosted mode.
- Trace buffer External mode.
- Trace buffer management.
- Synchronization and the Trace Buffer Unit.
- Trace synchronization and memory barriers.
- Trace of Speculative execution.
- Trace in Debug state.
- Synchronization litmus tests.
- UNPREDICTABLE behavior.