## K13.6 Built-in functions

This section describes:

- Bitstring manipulation functions.
- Arithmetic functions.

## K13.6.1 Bitstring manipulation functions

The following bitstring manipulation functions are defined:

## K13.6.1.1 Bitstring length and most significant bit

If x is a bitstring:

- The bitstring length function Len(x) returns the length of x as an integer.

## K13.6.1.2 Bitstring concatenation and replication

If x is a bitstring and n is an integer with n &gt;= 0 :

- Replicate(x, n) is the bitstring of length n*Len(x) consisting of n copies of x concatenated together.
- Zeros(n) = Replicate('0', n) .
- Ones(n) = Replicate('1', n) .

## K13.6.1.3 Bitstring count

If x is a bitstring, BitCount(x) is an integer result equal to the number of bits of x that are ones.

## K13.6.1.4 Testing a bitstring for being all zero or all ones

If x is a bitstring:

- IsZero(x) produces TRUE if all of the bits of x are zeros and FALSE if any of them are ones
- IsZeroBit(x) produces '1' if all of the bits of x are zeros and '0' if any of them are ones.

IsOnes(x) and IsOnesBit(x) work in the corresponding ways. This means:

```
IsZero(x) = (BitCount(x) == 0) IsOnes(x) = (BitCount(x) == Len(x)) IsZeroBit(x) = if IsZero(x) then '1' else '0' IsOnesBit(x) = if IsOnes(x) then '1' else '0'
```

## K13.6.1.5 Lowest and highest set bits of a bitstring

If x is a bitstring, and N = Len(x) :

- LowestSetBit(x) is the minimum bit number of any of the bits of x that are ones. If all of its bits are zeros, LowestSetBit(x) = N .
- HighestSetBit(x) is the maximum bit number of any of the bits of x that are ones. If all of its bits are zeros, HighestSetBit(x) = -1 .
- CountLeadingZeroBits(x) is the number of zero bits at the left end of x, in the range 0 to N . This means: CountLeadingZeroBits(x) = N - 1 - HighestSetBit(x) .
- CountLeadingSignBits(x) is the number of copies of the sign bit of x at the left end of x, excluding the sign bit itself, and is in the range 0 to N -1. This means:

CountLeadingSignBits(x) = CountLeadingZeroBits(x&lt;N-1:1&gt; EOR x&lt;N-2:0&gt;) .

## K13.6.1.6 Zero-extension and sign-extension of bitstrings

If x is a bitstring and i is an integer, then ZeroExtend(x, i) is x extended to a length of i bits, by adding sufficient zero bits to its left. That is, if i == Len(x) , then ZeroExtend(x, i) = x , and if i &gt; Len(x) , then:

```
ZeroExtend(x, i) = Replicate('0', i-Len(x)) :
```

```
x
```

If x is a bitstring and i is an integer, then SignExtend(x, i) is x extended to a length of i bits, by adding sufficient copies of its leftmost bit to its left. That is, if i == Len(x) , then SignExtend(x, i) = x , and if i &gt; Len(x) , then:

```
SignExtend(x, i) = Replicate(TopBit(x), i-Len(x)) : x
```

It is a pseudocode error to use either ZeroExtend(x, i) or SignExtend(x, i) in a context where it is possible that i &lt; Len(x) .

## K13.6.1.7 Converting bitstrings to integers

If x is a bitstring, SInt() is the integer whose two's complement representation is x .

UInt() is the integer whose unsigned representation is x .

## K13.6.2 Arithmetic functions

This section defines built-in arithmetic functions.

## K13.6.2.1 Absolute value

If x is either of type real or integer, Abs(x) returns the absolute value of x . The result is the same type as x .

## K13.6.2.2 Rounding and aligning

If x is a real:

- RoundDown(x) produces the largest integer n such that n &lt;= x .
- RoundUp(x) produces the smallest integer n such that n &gt;= x .
- RoundTowardsZero(x) produces:
- -RoundDown(x) if x &gt; 0.0 .
- -0 if x == 0.0 .
- -RoundUp(x) if x &lt; 0.0 .

If x and y are both of type integer , Align(x, y) = y * (x DIV y) , and is of type integer .

If x is of type bitstring and y is of type integer , Align(x, y) = (Align(UInt(x), y))&lt;Len(x)-1:0&gt; , and is a bitstring of the same length as x .

It is a pseudocode error to use either form of Align(x, y) in any context where y can be 0. In practice, Align(x, y) is only used with y a constant power of two, and the bitstring form used with y = 2^n has the effect of producing its argument with its n low-order bits forced to zero.

## K13.6.2.3 Maximum and minimum

If x and y are integers or reals, then Max(x, y) and Min(x, y) are their maximum and minimum respectively. x and y must both be of type integer or of type real. The function returns a value of the same type as its operands.