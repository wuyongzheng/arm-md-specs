## D18.1 About the Statistical Profiling Extension sample records

The Statistical Profiling Extension sample record format version is identified by PMSIDR\_EL1.Format. The architecture currently defines only version 0.

Note

Armv8.7 defines the SPE sample record format version, allowing future architecture updates to extend or change the record format. PMSIDR\_EL1.Format was previously a res0 field in a read-only register. Software that reads and checks PMSIDR\_EL1.Format on any implementation prior to Armv8.7 that includes SPE will read a value indicating format version 0 is supported.

The sample record format version 0 is self-describing and extensible. This format allows software to parse profile data even when that profile data contains extended information.

The Statistical Profiling Extension writes a series of sample records to memory, each record consisting of a sequence of packets, and each packet consisting of:

- One or two header bytes.
- Zero, 1, 2, 4, or 8 payload bytes.

## D18.1.1 Headers

The first header byte encodes the number of payload bytes:

0x00 -0x1F Single byte header, no payload.

0x20 -0x3F First byte of extended header. Second byte encodes the payload length.

0x40 -0x4F , 0x80 -0x8F , 0xC0 -0xCF

Header with an 8-bit payload.

0x50 -0x5F , 0x90 -0x9F , 0xD0 -0xDF

Header with a 16-bit payload.

0x60 -0x6F , 0xA0 -0xAF , 0xE0 -0xEF

Header with a 32-bit payload.

0x70 -0x7F , 0xB0 -0xBF , 0xF0 -0xFF

Header with a 64-bit payload.

## D18.1.2 Records

Arecord consists of multiple packets. A record comprises, in ascending address order:

- Asequence of headers, each followed by their payload byte or bytes.
- Either:
- -An End packet header.
- -ATimestamp packet.

Figures in this chapter show each packet as a sequence of bytes. Figure D18-1 shows how bytes are stored in memory in increasing addresses from left to right.

Figure D18-1 Convention for packet description

| First byte    | 1    | 2    | 3                   | 4    | Last Byte       |
|---------------|------|------|---------------------|------|-----------------|
| Header        | Data | Data | Header (8-bit data) | Data | 0x01 End Packet |
| (16-bit data) | LSB  | MSB  | Header (8-bit data) | Data | 0x01 End Packet |

| First Byte           | 1    | 2    | 3                   | 4    | 5                     | 6        | ...   | 12         | Last Byte   |
|----------------------|------|------|---------------------|------|-----------------------|----------|-------|------------|-------------|
| Header (16-bit data) | Data | Data | Header (8-bit data) | Data | 0x71 Timestamp Packet | TS [7:0] | ...   | TS [55:48] | TS [63:56]  |
| Header (16-bit data) | LSB  | MSB  | Header (8-bit data) | Data |                       | TS [7:0] | ...   | TS [55:48] | TS [63:56]  |

In some sections, the figures are split into separate figures for the header byte and payload bytes. For instance, where the number of payload bytes varies according to a field in the header.

The header bytes and payload bytes are described in ascending memory address order. Within a payload value, values are in little-endian byte order.

The size of the access granule for writes to the Profiling Buffer by the Statistical Profiling Unit is IMPLEMENTATION DEFINED, up to a maximum of 2KB. The size of the access granule can vary from time to time.

## D18.1.3 Protocol framing packets and forwards compatibility

The padding header, Timestamp packet, and end packet are protocol framing packets that frame the records created by the Statistical Profiling Unit. Only padding headers are permitted between records.

Note

PMBIDR\_EL1.Align defines a minimum alignment for records. However, implementations must nevertheless create a valid protocol stream that can be parsed without knowledge of the minimum alignment.

The packet types are described in the following sections. Software must ignore unknown packets, using the size field encoded in the header. This includes packets containing reserved values in fields.

The following sections give an overview of the Statistical Profiling Unit packets output to a memory-mapped Profiling Buffer or Device memory:

- Statistical Profiling Extension protocol packet headers

## D18.1.4 Statistical Profiling Extension protocol packet headers

## D18.1.4.1 8-bit headers

For Address packets and Counter packets, the 8-bit header format is described as the Short format .

## Table D18-1 8-bit header encodings

|   [7] |   [6] |   [5] |   [4] |   [3] |   [2] |   [1] |   [0] | Description      |
|-------|-------|-------|-------|-------|-------|-------|-------|------------------|
|     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 | Padding          |
|     0 |     0 |     0 |     0 |     0 |     0 |     0 |     1 | End packet       |
|     0 |     1 |     1 |     1 |     0 |     0 |     0 |     1 | Timestamp packet |

|   [7] |   [6] | [5]   | [4]   |   [3] | [2]   | [1]   | [0]   | Description                   |
|-------|-------|-------|-------|-------|-------|-------|-------|-------------------------------|
|     0 |     1 | x     | x     |     0 | 0     | 1     | 0     | Events packet                 |
|     0 |     1 | x     | x     |     0 | 0     | 1     | 1     | Data Source packet            |
|     0 |     1 | 1     | 0     |     0 | 1     | x     | x     | Context packet                |
|     0 |     1 | 0     | 0     |     1 | 0     | x     | x     | Operation Type packet         |
|     1 |     0 | 1     | 1     |     0 | x     | x     | x     | Address packet (Short format) |
|     1 |     0 | 0     | 1     |     1 | x     | x     | x     | Counter packet (Short format) |

## D18.1.4.2 16-bit headers

For Address packets and Counter packets, the 16-bit header format is described as the Extended format .

## Table D18-2 16-bit header encodings

| Byte 0   | Byte 0   | Byte 1 Description   | Byte 1 Description   | Byte 1 Description   | Byte 1 Description   | Byte 1 Description   | Byte 1 Description   | Byte 1 Description   | Byte 1 Description   | Byte 1 Description   | Byte 1 Description   | Byte 1 Description   | Byte 1 Description   | Byte 1 Description   | Byte 1 Description   | Byte 1 Description   |
|----------|----------|----------------------|----------------------|----------------------|----------------------|----------------------|----------------------|----------------------|----------------------|----------------------|----------------------|----------------------|----------------------|----------------------|----------------------|----------------------|
| [7]      | [6]      | [5]                  | [4]                  | [3]                  | [2]                  | [1]                  | [0]                  | [7]                  | [6]                  | [5]                  | [4]                  | [3]                  | [2]                  | [1]                  | [0]                  |                      |
| 0        | 0        | 1                    | 0                    | 0                    | 0                    | x                    | x                    | 1                    | 0                    | 1                    | 1                    | 0                    | x                    | x                    | x                    | Address packet       |
| 0        | 0        | 1                    | 0                    | 0                    | 0                    | x                    | x                    | 1                    | 0                    | 0                    | 1                    | 1                    | x                    | x                    | x                    | Counter packet       |