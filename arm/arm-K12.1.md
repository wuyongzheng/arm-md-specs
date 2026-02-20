## K12.1 Properties of the generated random number

When FEAT\_RNG is implemented, reads of the RNDR and RNDRRS registers return 64-bit random numbers. The RNDRand RNDRRS implementation should conform to approved standards that are appropriate for the market requirements.

For example, the NIST SP 800-90 series of documents:

- SP 800-90A Recommendation for Random Number Generation Using Deterministic Random Bit Generators.
- SP 800-90B Recommendation for the Entropy Sources Used for Random Bit Generation.
- SP 800-90C Recommendation for Random Bit Generator Constructions.

## Note

- Since an entropy source can only generate random bits at a limited rate, the random number bits are commonly collected in an 'entropy pool' until needed. An implementation should ensure that lower privileged software cannot impact the performance of higher privileged software by entirely draining this 'entropy pool'. The refill time cost of the 'entropy pool' should be paid for by the persistent caller.
- When FEAT\_RNG\_TRAP is implemented, reads of the RNDR and RNDRRS registers may be trapped to EL3. For more information about this trapping behavior, see control fields ID\_AA64PFR1\_EL1.RNDR\_trap and SCR\_EL3.TRNDR

## Appendix K13 Arm Pseudocode Definition

This appendix provides a definition of the pseudocode that is used in this manual, and defines some helper procedures and functions that are used by pseudocode. It contains the following sections:

- About the Arm pseudocode.

- Pseudocode for instruction descriptions.

- Data types.

- Operators.

- Statements and control structures.

- Built-in functions.

- Miscellaneous helper procedures and functions.

- Arm pseudocode definition index.

Note

This appendix is not a formal language definition for the pseudocode. It is a guide to help understand the use of Arm pseudocode. This appendix is not complete. Changes are planned for future releases.