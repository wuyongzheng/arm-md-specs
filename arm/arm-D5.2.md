## D5.2 Summary list of ETE packets

Table D5-3 lists the ETE packets ordered by the header byte.

## Table D5-3 ETE Packets

| Header byte   | Name                                             | Purpose                                                                                                  |
|---------------|--------------------------------------------------|----------------------------------------------------------------------------------------------------------|
| 00000000      | Alignment Synchronization Packet                 | Identifies a packet boundary.                                                                            |
| 00000000      | Discard Packet                                   | Indicates a Discard element .                                                                            |
| 00000000      | Overflow Packet                                  | Indicates that a trace unit buffer overflow has occurred.                                                |
| 00000001      | Trace Info Packet                                | Resets trace compression to a known architectural state.                                                 |
| 0000001x      | Timestamp Packet                                 | Indicates a Timestamp element .                                                                          |
| 00000100      | Trace On Packet                                  | Indicates that there has been a discontinuity in the trace element stream.                               |
| 00000110      | PE Reset Packet                                  | Indicates that a PE Reset has occurred.                                                                  |
| 00000110      | Transaction Failure Packet                       | Indicates that a Transaction Failure has occurred.                                                       |
| 00000110      | Exception 32-bit Address IS0 with Context Packet | Indicates that an exception has occurred.                                                                |
| 00000110      | Exception 32-bit Address IS1 with Context Packet | Indicates that an exception has occurred.                                                                |
| 00000110      | Exception 64-bit Address IS0 with Context Packet | Indicates that an exception has occurred.                                                                |
| 00000110      | Exception 64-bit Address IS1 with Context Packet | Indicates that an exception has occurred.                                                                |
| 00000110      | Exception Exact Match Address Packet             | Indicates that an exception has occurred.                                                                |
| 00000110      | Exception Short Address IS0 Packet               | Indicates that an exception has occurred.                                                                |
| 00000110      | Exception Short Address IS1 Packet               | Indicates that an exception has occurred.                                                                |
| 00000110      | Exception 32-bit Address IS0 Packet              | Indicates that an exception has occurred.                                                                |
| 00000110      | Exception 32-bit Address IS1 Packet              | Indicates that an exception has occurred.                                                                |
| 00000110      | Exception 64-bit Address IS0 Packet              | Indicates that an exception has occurred.                                                                |
| 00000110      | Exception 64-bit Address IS1 Packet              | Indicates that an exception has occurred.                                                                |
| 00001001      | Instrumentation Packet                           | Indicates an Instrumentation element .                                                                   |
| 00001010      | Transaction Start Packet                         | Indicates that the PE has started to execute in Transactional state.                                     |
| 00001011      | Transaction Commit Packet                        | Indicates that the PE has successfully finished an outer transaction and is leaving Transactional state. |
| 00001100      | Cycle Count Format 2_0 small commit Packet       | Indicates a Commit element and a Cycle Count element .                                                   |
| 00001101      | Cycle Count Format 2_1 Packet                    | Indicates a Cycle Count element .                                                                        |
| 00001101      | Cycle Count Format 2_0 large commit Packet       | Indicates a Commit element and a Cycle Count element .                                                   |
| 00001110      | Cycle Count Format 1_1 with count Packet         | Indicates a Cycle Count element .                                                                        |
| 00001110      | Cycle Count Format 1_0 with count Packet         | Indicates zero or one Commit elements followed by a Cycle Count element                                  |
| 00001111      | Cycle Count Format 1_1 unknown count Packet      | Indicates a Cycle Count element .                                                                        |

| Header byte   | Name                                          | Purpose                                                                                                              |
|---------------|-----------------------------------------------|----------------------------------------------------------------------------------------------------------------------|
| 00001111      | Cycle Count Format 1_0 unknown count Packet   | Indicates zero or one Commit elements followed by a Cycle Count element with an UNKNOWN cycle count value. &#124;    |
| 000100xx      | Cycle Count Format 3_1 Packet                 | Indicates a Cycle Count element .                                                                                    |
| 0001xxxx      | Cycle Count Format 3_0 Packet                 | Indicates a Commit element and a Cycle Count element .                                                               |
| 00101101      | Commit Packet                                 | Indicates a Commit element .                                                                                         |
| 0010111x      | Cancel Format 1 Packet                        | Indicates a Cancel element optionally followed by a Mispredict element .                                             |
| 001100xx      | Mispredict Packet                             | Indicates 0-2 E orN Atom elements followed by one Mispredict element .                                               |
| 001101xx      | Cancel Format 2 Packet                        | Indicates zero or more E orN Atom elements followed by a Cancel element and a Mispredict element .                   |
| 00111xxx      | Cancel Format 3 Packet                        | Indicates zero or one E Atom element followed by a Cancel element with a payload of 2-5 and one Mispredict element . |
| 01110000      | Ignore Packet                                 | To align packet boundary to memory boundary.                                                                         |
| 0111xxxx      | Event Packet                                  | Indicates 1-4 Event elements .                                                                                       |
| 10000000      | Context Same Packet                           | Indicates a Context element .                                                                                        |
| 10000001      | Context Packet                                | Indicates a Context element .                                                                                        |
| 10000010      | Target Address with Context 32-bit IS0 Packet | Indicates a Target Address element and a Context element .                                                           |
| 10000011      | Target Address with Context 32-bit IS1 Packet | Indicates a Target Address element and a Context element .                                                           |
| 10000101      | Target Address with Context 64-bit IS0 Packet | Indicates a Target Address element and a Context element .                                                           |
| 10000110      | Target Address with Context 64-bit IS1 Packet | Indicates a Target Address element and a Context element .                                                           |
| 10001000      | Timestamp Marker Packet                       | Indicates a Timestamp Marker element .                                                                               |
| 100100xx      | Target Address Exact Match Packet             | Indicates a Target Address element .                                                                                 |
| 10010101      | Target Address Short IS0 Packet               | Indicates a Target Address element .                                                                                 |
| 10010110      | Target Address Short IS1 Packet               | Indicates a Target Address element .                                                                                 |
| 10011010      | Target Address 32-bit IS0 Packet              | Indicates a Target Address element .                                                                                 |
| 10011011      | Target Address 32-bit IS1 Packet              | Indicates a Target Address element .                                                                                 |
| 10011101      | Target Address 64-bit IS0 Packet              | Indicates a Target Address element .                                                                                 |
| 10011110      | Target Address 64-bit IS1 Packet              | Indicates a Target Address element .                                                                                 |
| 101000xx      | Qwith Exact match address Packet              | Indicates that some instructions have executed with an address of the next instruction.                              |
| 10100101      | Qshort address IS0 Packet                     | Indicates that some instructions have executed with an address of the next instruction.                              |
| 10100110      | Qshort address IS1 Packet                     | Indicates that some instructions have executed with an address of the next instruction.                              |
| 10101010      | Q32-bit address IS0 Packet                    | Indicates that some instructions have executed with an address of the next instruction.                              |
| 10101011      | Q32-bit address IS1 Packet                    | Indicates that some instructions have executed with an address of the next instruction.                              |
| 10101100      | Qwith count Packet                            | Indicates that some instructions have executed.                                                                      |
| 10101111      | QPacket                                       | Indicates that some instructions have executed, without a count of the number of instructions.                       |

| Header byte   | Name                              | Purpose                                                                                |
|---------------|-----------------------------------|----------------------------------------------------------------------------------------|
| 101100xx      | Source Address Exact Match Packet | Indicates the source address of a P0 instruction , and that the instruction was taken. |
| 10110100      | Source Address Short IS0 Packet   | Indicates the source address of a P0 instruction , and that the instruction was taken. |
| 10110101      | Source Address Short IS1 Packet   | Indicates the source address of a P0 instruction , and that the instruction was taken. |
| 10110110      | Source Address 32-bit IS0 Packet  | Indicates the source address of a P0 instruction , and that the instruction was taken. |
| 10110111      | Source Address 32-bit IS1 Packet  | Indicates the source address of a P0 instruction , and that the instruction was taken. |
| 10111000      | Source Address 64-bit IS0 Packet  | Indicates the source address of a P0 instruction , and that the instruction was taken. |
| 10111001      | Source Address 64-bit IS1 Packet  | Indicates the source address of a P0 instruction , and that the instruction was taken. |
| 110101xx      | Atom Format 5.2 Packet            | Indicates five Atom elements .                                                         |
| 110110xx      | Atom Format 2 Packet              | Indicates two Atom elements .                                                          |
| 110111xx      | Atom Format 4 Packet              | Indicates four Atom elements .                                                         |
| 11110101      | Atom Format 5.1 Packet            | Indicates five Atom elements .                                                         |
| 1111011x      | Atom Format 1 Packet              | Indicates one Atom element .                                                           |
| 11111xxx      | Atom Format 3 Packet              | Indicates three Atom elements .                                                        |
| 11xxxxxx      | Atom Format 6 Packet              | Indicates 3-23 E Atom elements , plus a subsequent E Atom orN Atom element .           |