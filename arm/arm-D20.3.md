## D20.3 Generating error exceptions

| R VJRKF   | An Error exception is generated when a detected error is signaled to the PE as an in-band error response to an architecturally-executed memory access or cache maintenance operation. This includes any explicit data access, instruction fetch, translation table walk, or hardware update to the translation tables made by an architecturally-executed instruction.   |
|-----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| I PJHZS   | An Error exception is taken as an asynchronous SError exception, a synchronous External Data Abort exception, or a synchronous External Instruction Abort exception.                                                                                                                                                                                                     |
| R MBNBH   | It is IMPLEMENTATION DEFINED whether an Error exception can be generated for an error that is consumed by hardware speculation or prefetching by a PE, but that is not committed to the architecturally visible state of the PE.                                                                                                                                         |
| R SHKJB   | It is IMPLEMENTATION DEFINED whether an Error exception can be generated for a detected error that is deferred.                                                                                                                                                                                                                                                          |
| R GVWJD   | It is IMPLEMENTATION DEFINED whether an Error exception can be generated for a detected error that is corrected.                                                                                                                                                                                                                                                         |
| R FNVVJ   | An Error exception can also be generated for IMPLEMENTATION DEFINED causes. An Error exception generated for an IMPLEMENTATION DEFINED cause is taken as an SError exception.                                                                                                                                                                                            |

Example D20-11

An error is detected and neither corrected nor deferred to the PE, and signaled to the PE by means other than an in-band error response, such as a wired SError exception pin. Asserting the SError exception pin causes the PE to generate an SError exception.

Example D20-12

An error is detected by the PE in the PE state, or in the result of a calculation performed by the PE. The detected error generates an SError exception.

See also:

- Exceptions.
- Taking error exceptions.

IZXHDP