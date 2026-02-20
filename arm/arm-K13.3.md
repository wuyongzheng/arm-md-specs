## K13.3 Data types

This section describes:

- General data type rules.
- Bitstrings.
- Integers.
- Reals.
- Booleans.
- Enumerations.
- Structures.
- Tuples.
- Arrays.

## K13.3.1 General data type rules

Arm architecture pseudocode is a strongly typed language. Every literal and variable is of one of the following types:

- Bitstring.
- Integer.
- Boolean.
- Real.
- Enumeration.
- Tuple.
- Struct.
- Array.

The type of a literal is determined by its syntax. A variable can be assigned to without an explicit declaration. The variable implicitly has the type of the assigned value. For example, the following assignments implicitly declare the variables x , y and z to have types integer, bitstring of length 1, and Boolean, respectively.

```
x = 1; y = '1'; z = TRUE;
```

Variables can also have their types declared explicitly by preceding the variable name with the name of the type. The following example declares explicitly that a variable named count is an integer.

```
integer count;
```

This is most often done in function definitions for the arguments and the result of the function.

The remaining subsections describe each data type in more detail.

## K13.3.2 Bitstrings

This section describes the bitstring data type.

| K13.3.2.1   | Syntax                                     |
|-------------|--------------------------------------------|
| bits(N)     | The type name of a bitstring of length N . |
| bit         | Asynonym of bits(1) .                      |

## K13.3.4 Reals

## K13.3.2.2 Description

Abitstring is a finite-length string of 0s and 1s. Each length of bitstring is a different type. The minimum permitted length of a bitstring is 0.

Bitstring constants literals are written as a single quotation mark, followed by the string of 0s and 1s, followed by another single quotation mark. For example, the two constants literals of type bit are '0' and '1' . Spaces can be included in bitstrings for clarity.

The bits in a bitstring are numbered from left to right N -1 to 0. This numbering is used when accessing the bitstring using bitslices. In conversions to and from integers, bit N -1 is the MSByte and bit 0 is the LSByte. This order matches the order in which bitstrings derived from encoding diagrams are printed.

Every bitstring value has a left-to-right order, with the bits being numbered in standard little-endian order. That is, the leftmost bit of a bitstring of length N is bit ( N -1) and its right-most bit is bit 0. This order is used as the most-significant-to-least-significant bit order in conversions to and from integers. For bitstring constants and bitstrings that are derived from encoding diagrams, this order matches the way that they are printed.

Bitstrings are the only concrete data type in pseudocode, corresponding directly to the contents values that are manipulated in registers, memory locations, and instructions. All other data types are abstract.

## K13.3.3 Integers

This section describes the data type for integer numbers.

## K13.3.3.1 Syntax

integer

The type name for the integer data type.

## K13.3.3.2 Description

Pseudocode integers are unbounded in size and can be either positive or negative. That is, they are mathematical integers rather than what computer languages and architectures commonly call integers. Computer integers are represented in pseudocode as bitstrings of the appropriate length, and the pseudocode provides functions to interpret those bitstrings as integers.

Integer literals are normally written in decimal form, such as 0 , 15 , -1234 . They can also be written in C-style hexadecimal form, such as 0x55 or 0x8000\_0000 . Hexadecimal integer literals are treated as positive unless they have a preceding minus sign. For example, 0x8000\_0000 is the integer +2 31 . If -2 31 needs to be written in hexadecimal, it must be written as -0x8000\_0000 .

This section describes the data type for real numbers.

## K13.3.4.1 Syntax

real

The type name for the real data type.

## K13.3.4.2 Description

Pseudocode reals are unbounded in size and precision. That is, they are mathematical real numbers, not computer floating-point numbers. Computer floating-point numbers are represented in pseudocode as bitstrings of the appropriate length, and the pseudocode provides functions to interpret those bitstrings as reals.

Real constant literals are written in decimal form with a decimal point. This means 0 is an integer constant literal, but 0.0 is a real constant literal.

## K13.3.5 Booleans

This section describes the Boolean data type.

## K13.3.5.1 Syntax

boolean

The type name for the Boolean data type.

TRUE or FALSE The two values a Boolean variable can take.

## K13.3.5.2 Description

ABoolean is a logical TRUE or FALSE value.

Note

This is not the same type as bit , which is a bitstring of length 1. A Boolean can only take on one of two values: TRUE or FALSE .

## K13.3.6 Enumerations

This section describes the enumeration data type.

## K13.3.6.1 Syntax and examples

enumeration Keyword to defined a new enumeration type.

enumeration Example {Example\_One, Example\_Two, Example\_Three};

Adefinition of a new enumeration called Example , which can take on the values Example\_One , Example\_Two , Example\_Three .

## K13.3.6.2 Description

An enumeration is a defined set of named values.

An enumeration must contain at least one named value. A named value must not be shared between enumerations.

Enumerations must be defined explicitly, although a variable of an enumeration type can be declared implicitly by assigning one of the named values to it. By convention, each named value starts with the name of the enumeration followed by an underscore. The name of the enumeration is its type name , or type , and the named values are its possible values .

## K13.3.7 Structures

This section describes the structure data type.

## K13.3.7.1 Syntax and examples

type

The keyword used to declare the structure data type.

type ShiftSpec is (bits(2) shift, integer amount)

An example definition for a new structure called ShiftSpec that contains an bitstring member called shift and a integer member named amount . Structure definitions must not be terminated with a semicolon.

ShiftSpec abc;

Adeclaration of a variable named abc of type ShiftSpec .

abc.shift

Syntax to refer to the individual members within the structure variable.

## K13.3.8 Tuples

## K13.3.7.2 Description

Astructure is a compound data type composed of one or more data items. The data items can be of different data types. This can include compound data types. The data items of a structure are called its members and are named.

In the syntax section, the example defines a structure called ShiftSpec with two members. The first is a bitstring of length 2 named shift and the second is an integer named amount . After declaring a variable of that type named abc , the members of this structure are referred to as abc.shift and abc.amount .

Every definition of a structure creates a different type, even if the number and type of their members are identical. For example:

```
type ShiftSpec1 is (bits(2) shift, integer type ShiftSpec2 is (bits(2) shift, integer
```

```
amount) amount)
```

ShiftSpec1 and ShiftSpec2 are two different types despite having identical definitions. This means that the value in a variable of type ShiftSpec1 cannot be assigned to variable of type ShiftSpec2 .

This section describes the tuple data type.

## K13.3.8.1 Examples

(bits(32) shifter\_result, bit shifter\_carry\_out)

An example of the tuple syntax.

```
(shift_t, shift_n) = ('00', 0);
```

An example of assigning values to a tuple.

## K13.3.8.2 Description

Atuple is an ordered set of data items, separated by commas and enclosed in parentheses. The items can be of different types and a tuple must contain at least one data item.

Tuples are often used as the return type for functions that return multiple results. For example, in the syntax section, the example tuple is the return type of the function Shift\_C() , which performs a standard A32/T32 shift or rotation. Its return type is a tuple containing two data items, with the first of type bits(32) and the second of type bit .

Each tuple is a separate compound data type. The compound data type is represented as a comma-separated list of ordered data types between parentheses. This means that the example tuple at the start of this section is of type (bits(32), bit) . The general principle that types can be implied by an assignment extends to implying the type of the elements in the tuple. For example, in the syntax section, the example assignment implicitly declares:

- shift\_t to be of type bits(2) .
- shift\_n to be of type integer .
- (shift\_t, shift\_n) to be a tuple of type (bits(2), integer) .

## K13.3.9 Arrays

This section describes the array data type.

## K13.3.9.1 Syntax

array

The type name for the array data type.

array data\_type array\_name[A..B]

```
;
```

Declaration of an array of type data\_type , which might be compound data type. It is named array\_name and is indexed with an integer range from A to B .

## K13.3.9.2 Description

An array is an ordered set of fixed size containing items of a single data type. This can include compound data types. Pseudocode arrays are indexed by either enumerations or integer ranges. An integer range is represented by the lower inclusive end of the range, then .. , then the upper inclusive end of the range.

For example:

The following example declares an array of 31 bitstrings of length 64, indexed from 0 to 30.

```
array bits(64) _R[0..30];
```

Arrays are always explicitly declared, and there is no notation for a constant literal array. Arrays always contain at least one element data item, because:

- Enumerations always contain at least one symbolic constant named value.
- Integer ranges always contain at least one integer.

An array declared with an enumeration type as the index must be accessed using enumeration values of that enumeration type. An array declared with an integer range type as the index must be accessed using integer values from that inclusive range. Accessing such an array with an integer value outside of the range is a coding error.

Arrays do not usually appear directly in pseudocode. The items that syntactically look like arrays in pseudocode are usually array-like functions such as R[i] , MemU[address, size] or Elem[vector, i, size] . These functions package up and abstract additional operations normally performed on accesses to the underlying arrays, such as register banking, memory protection, endian-dependent byte ordering, exclusive-access housekeeping and Advanced SIMD element processing. See Function and procedure calls.