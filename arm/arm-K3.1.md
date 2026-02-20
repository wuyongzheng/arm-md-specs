## K3.1 Configurations

IYCKVP

For optional features not described here, it is IMPLEMENTATION DEFINED whether the feature is implemented. For features which have an IMPLEMENTATION DEFINED size or number, and are not described here, the size or number of that feature is IMPLEMENTATION DEFINED.

| Parameter   | Description                                            | Configuration                                                              |
|-------------|--------------------------------------------------------|----------------------------------------------------------------------------|
| ATBTRIG     | ATB Trigger Support                                    | Yes, if ATB is implemented                                                 |
| NUMACPAIRS  | Address Comparator pairs                               | 4                                                                          |
| NUMCIDC     | Context Identifier Comparators                         | >= 1                                                                       |
| NUMVMIDC    | Virtual Context Identifier Comparators                 | >= 1, if EL2 is implemented                                                |
| NUMCNTR     | Number of Counters                                     | 2                                                                          |
| NUMEVENT    | Number of ETEEvents                                    | 4                                                                          |
| NUMEXTINSEL | Number of External Input Selectors                     | 4                                                                          |
| NUMRSPAIR   | Number of Resource selection pairs                     | >= 8                                                                       |
| NUMSEQSTATE | Number of Sequencer states                             | 4                                                                          |
| NUMSSCC     | Number of Single-shot Comparator Controls              | >= 1                                                                       |
| RETSTACK    | Return stack                                           | Yes                                                                        |
| STALLCTL    | PE stalling capability                                 | Yes                                                                        |
| TRACEIDSIZE | Trace ID size                                          | 7-bits, if ATB is implemented                                              |
| CCITMIN     | Cycle count minimum threshold                          | 4                                                                          |
| CCSIZE      | Cycle counter size                                     | >= 12                                                                      |
| WFXMODE     | WFI , WFIT , WFE , and WFET instruction classification | WFI , WFIT , WFE , and WFET instructions are classified as P0 instructions |

## Appendix K4 Stages of Execution

This appendix shows the relationship between the stages of execution. It contains the following sections:

- Stages of execution.