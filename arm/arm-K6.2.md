## K6.2 Gray count scheme for timer distribution scheme

The distribution of the Counter value using a Gray code provides a relatively simple mechanism to avoid any danger of the count being sampled with an intermediate value even if the clocking is asynchronous. It has a further advantage that the distribution is relatively low power, since only one bit changes on the main distribution wires for each clock tick.

Asuitable Gray-coding scheme can be achieved with the following logic:

```
Gray = Count EOR ('0':Count<N:1>) Count<N> = Gray<N> for i = N-1 downto 0 Count<i> = Gray<i> EOR Count<i+1>
```

This is for an N+1 bit counter, where Count is a conventional binary count value, and Gray is the corresponding Gray count value.

## Appendix K7 Legacy Instruction Syntax for AArch32 Instruction Sets

This appendix describes the legacy instruction syntax in the Arm instruction sets, and their Unified Assembler Language (UAL) equivalents. It contains the following section:

- Legacy Instruction Syntax.