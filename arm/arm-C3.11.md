## C3.11 Data processing - SME, SME2

The following subsections describe the SME, SME2, and SME2.1 processing instructions:

- Clamp to minimum/maximum.
- Dot product.
- Vertical dot product.
- Element concatenate and interleave.
- Floating-point conversions.
- Floating-point round.
- Floating-point adjust exponent.
- Lookup table.
- Move operations.
- Multi-vector arithmetic.
- Multi-vector minimum/maximum.
- Multi-vector multiply.
- Multi-vector multiply-accumulate.
- Multi-vector multiply high.
- Multi-vector select.
- Multi-vector shift and convert.
- Outer product.
- Quarter-tile outer product.
- Structured sparsity outer product.
- Stack frame operations.
- Unpack and extend.
- Zero operations.

## C3.11.1 Clamp to minimum/maximum

Clamp each element in the destination vectors to between the minimum value in the corresponding element of the first source vector and the maximum value in the corresponding element of the second source vector and destructively place the clamped results in the corresponding elements of the destination vectors.

## C3.11.1.1 Floating-point clamp to minimum/maximum

## Table C3-242 SME2 Floating-point clamp to minimum/maximum instructions

| Mnemonic   | Instruction                                                          | See     |
|------------|----------------------------------------------------------------------|---------|
| BFCLAMP    | Multi-vector BFloat16 floating-point clamp to minimum/maximum number | BFCLAMP |
| FCLAMP     | Multi-vector floating-point clamp to minimum/maximum number          | FCLAMP  |

## C3.11.1.2 Integer clamp to minimum/maximum

## Table C3-243 SME2 Integer clamp to minimum/maximum instructions

| Mnemonic   | Instruction                                           | See    |
|------------|-------------------------------------------------------|--------|
| SCLAMP     | Multi-vector signed clamp to minimum/maximum vector   | SCLAMP |
| UCLAMP     | Multi-vector unsigned clamp to minimum/maximum vector | UCLAMP |

## C3.11.2 Floating-point dot product

Compute the dot product of two or four values held in the corresponding elements of the first source vectors and in the corresponding element of the second source vector. The widened dot product is then added to the corresponding element of the ZA single-vector groups.

## C3.11.2.1 BFloat16 floating-point dot product

## Table C3-244 BFloat16 floating-point dot product instructions

| Mnemonic   | Instruction                                                         | See                                 |
|------------|---------------------------------------------------------------------|-------------------------------------|
| BFDOT      | Multi-vector BFloat16 floating-point dot-product by indexed element | BFDOT (multiple and indexed vector) |
| BFDOT      | Multi-vector BFloat16 floating-point dot-product by vector          | BFDOT (multiple and single vector)  |
| BFDOT      | Multi-vector BFloat16 floating-point dot-product                    | BFDOT (multiple vectors)            |

## C3.11.2.2 Floating-point dot product

## Table C3-245 SME2 Floating-point Dot product instructions

| Mnemonic   | Instruction                                                               | See                                |
|------------|---------------------------------------------------------------------------|------------------------------------|
| FDOT       | Multi-vector half-precision floating-point dot-product by indexed element | FDOT (multiple and indexed vector) |
|            | Multi-vector half-precision floating-point dot-product by vector          | FDOT (multiple and single vector)  |
|            | Multi-vector half-precision floating-point dot-product                    | FDOT (multiple vectors)            |

## C3.11.2.3 FP8 floating-point dot product

The FP8 floating-point dot product instructions accumulate the dot product of two or four FP8 source elements into half-precision or single-precision destination elements. They generate a fused, downscaled sum-of-products and accumulate into each destination element, without intermediate rounding.

For these instructions, the unbounded intermediate sum-of-products is scaled by subtracting the value specified in FPMR.LSCALE from its unbounded exponent. For more information, see the instruction descriptions.

## Table C3-246 SME2 FP8 floating-point convert instructions

| Mnemonic   | Instruction                                                                          | See                                                    |
|------------|--------------------------------------------------------------------------------------|--------------------------------------------------------|
| FDOT       | Multi-vector 8-bit floating-point dot-product by indexed element to half-precision   | FDOT (2-way, multiple and indexed vector, FP8 to FP16) |
| FDOT       | Multi-vector 8-bit floating-point dot-product by vector to half-precision            | FDOT (2-way, multiple and single vector, FP8 to FP16)  |
| FDOT       | Multi-vector 8-bit floating-point dot-product to half-precision                      | FDOT (2-way, multiple vectors, FP8 to FP16)            |
| FDOT       | Multi-vector 8-bit floating-point dot-product by indexed element to single-precision | FDOT (4-way, multiple and indexed vector)              |
| FDOT       | Multi-vector 8-bit floating-point dot-product by vector to single-precision          | FDOT (4-way, multiple and single vector)               |
| FDOT       | Multi-vector 8-bit floating-point dot-product to single-precision                    | FDOT (4-way, multiple vectors)                         |

## C3.11.2.4 Integer dot product

## Table C3-247 SME2 Integer Dot product instructions

| Mnemonic   | Instruction                                                             | See                                                                                 |
|------------|-------------------------------------------------------------------------|-------------------------------------------------------------------------------------|
| SDOT       | Multi-vector signed integer dot-product by indexed element              | SDOT (2-way, multiple and indexed vector) SDOT (4-way, multiple and indexed vector) |
| SDOT       | Multi-vector signed integer dot-product by vector                       | SDOT (2-way, multiple and single vector) SDOT (4-way, multiple and single vector)   |
| SDOT       | Multi-vector signed integer dot-product                                 | SDOT (2-way, multiple vectors) SDOT (4-way, multiple vectors)                       |
| SUDOT      | Multi-vector signed by unsigned integer dot-product by indexed elements | SUDOT(multiple and indexed vector)                                                  |
| SUDOT      | Multi-vector signed by unsigned integer dot-product by vector           | SUDOT(multiple and single vector)                                                   |
| UDOT       | Multi-vector unsigned integer dot-product by indexed element            | UDOT(2-way, multiple and indexed vector) UDOT(4-way, multiple and indexed vector)   |
| UDOT       | Multi-vector unsigned integer dot-product by vector                     | UDOT(2-way, multiple and single vector) UDOT(4-way, multiple and single vector)     |
| UDOT       | Multi-vector unsigned integer dot-product                               | UDOT(2-way, multiple vectors) UDOT(4-way, multiple vectors)                         |
| USDOT      | Multi-vector unsigned by signed integer dot-product by indexed element  | USDOT(multiple and indexed vector)                                                  |
| USDOT      | Multi-vector unsigned by signed integer dot-product by vector           | USDOT(multiple and single vector)                                                   |
| USDOT      | Multi-vector unsigned by signed integer dot-product                     | USDOT(multiple vectors)                                                             |

## C3.11.3 Vertical dot product

Compute the vertical dot product of the corresponding values held in the first source vectors and in the corresponding elements of second source vector. The widened dot product is then added to the corresponding element of the ZA single-vector groups.

## C3.11.3.1 BFloat16 vertical dot product

## Table C3-248 SME2 BFloat16 floating-point vertical dot product instructions

| Mnemonic   | Instruction                                                                  | See    |
|------------|------------------------------------------------------------------------------|--------|
| BFVDOT     | Multi-vector BFloat16 floating-point vertical dot-product by indexed element | BFVDOT |

## C3.11.3.2 Floating-point vertical dot product

## Table C3-249 SME2 Floating-point vertical dot product instructions

| Mnemonic   | Instruction                                                                        | See                 |
|------------|------------------------------------------------------------------------------------|---------------------|
| FVDOT      | Multi-vector half-precision floating-point vertical dot-product by indexed element | FVDOT(FP16 to FP32) |

## C3.11.3.3 FP8 floating-point vertical dot product

For FP8 vertical dot product instructions, the unbounded intermediate sum-of-products is scaled by subtracting the value specified in FPMR.LSCALE from its unbounded exponent. For more information, see the instruction descriptions.

## Table C3-250 SME2 FP8 floating-point vertical dot product instructions

| Mnemonic   | Instruction                                                                                            | See                |
|------------|--------------------------------------------------------------------------------------------------------|--------------------|
| FVDOT      | Multi-vector 8-bit floating-point vertical dot-product by indexed element to half-precision            | FVDOT(FP8 to FP16) |
| FVDOTB     | Multi-vector 8-bit floating-point vertical dot-product by indexed element to single-precision (bottom) | FVDOTB             |
| FVDOTT     | Multi-vector 8-bit floating-point vertical dot-product by indexed element to single-precision (top)    | FVDOTT             |

## C3.11.3.4 Integer vertical dot product

## Table C3-251 SME2 Integer vertical dot product instructions

| Mnemonic   | Instruction                                                                     | See                       |
|------------|---------------------------------------------------------------------------------|---------------------------|
| SUVDOT     | Multi-vector signed by unsigned integer vertical dot-product by indexed element | SUVDOT                    |
| SVDOT      | Multi-vector signed integer vertical dot-product by indexed element             | SVDOT(2-way) SVDOT(4-way) |
| USVDOT     | Multi-vector unsigned by signed integer vertical dot-product by indexed element | USVDOT                    |
| UVDOT      | Multi-vector unsigned integer vertical dot-product by indexed element           | UVDOT(2-way) UVDOT(4-way) |

## C3.11.4 Element concatenate and interleave

Join elements from the source vectors and place them in the corresponding elements of the destination vectors.

## Table C3-252 SME2 Element concatenate/interleave instructions

| Mnemonic   | Instruction                                | See                                      |
|------------|--------------------------------------------|------------------------------------------|
| UZP        | Concatenate elements from four/two vectors | UZP (four registers) UZP (two registers) |
| ZIP        | Interleave elements from four/two vectors  | ZIP (four registers) ZIP (two registers) |

## C3.11.5 Floating-point conversions

Convert each element of the source vectors and place the results in the corresponding elements of the destination vectors.

## C3.11.5.1 Floating-point conversions

## Table C3-253 SME2 Floating-point conversion instructions

| Mnemonic   | Instruction                                                                               | See              |
|------------|-------------------------------------------------------------------------------------------|------------------|
| FCVT       | Multi-vector floating-point convert from single-precision to packed half-precision        | FCVT (narrowing) |
|            | Multi-vector floating-point convert from half-precision to single-precision (in-order)    | FCVT (widening)  |
| FCVTL      | Multi-vector floating-point convert from half-precision to deinterleaved single-precision | FCVTL            |
| FCVTN      | Multi-vector floating-point convert from single-precision to interleaved half-precision   | FCVTN            |
| FCVTZS     | Multi-vector floating-point convert to signed integer, rounding toward zero               | FCVTZS           |
| FCVTZU     | Multi-vector floating-point convert to unsigned integer, rounding toward zero             | FCVTZU           |

## C3.11.5.2 BFloat16 floating-point conversions

## Table C3-254 BFloat16 Floating-point conversion instructions

| Mnemonic   | Instruction                                                                              | See    |
|------------|------------------------------------------------------------------------------------------|--------|
| BFCVT      | Multi-vector floating-point convert from single-precision to packed BFloat16 format      | BFCVT  |
| BFCVTN     | Multi-vector floating-point convert from single-precision to interleaved BFloat16 format | BFCVTN |

## C3.11.5.3 FP8 floating-point conversions

Convert each floating-point element of the source vectors while scaling the value, and place the results in the corresponding elements of the destination vector.

For instructions that convert other floating-point formats to FP8 formats, each input element is scaled by adding the value specified in FPMR.NSCALE to its unbounded exponent during the conversion.

For instructions that convert FP8 formats to other floating-point formats, each input element is scaled by subtracting the value specified in FPMR.LSCALE or FPMR.LSCALE2 from its unbounded exponent during the conversion.

For more information, see the instruction descriptions.

## Table C3-255 FP8 floating-point conversion instructions

| Mnemonic         | Instruction                                                                                          | See                           |
|------------------|------------------------------------------------------------------------------------------------------|-------------------------------|
| BF1CVT, BF2CVT   | Multi-vector floating-point convert from 8-bit floating-point to BFloat16 (in-order)                 | BF1CVT, BF2CVT                |
| BF1CVTL, BF2CVTL | Multi-vector floating-point convert from 8-bit floating-point to deinterleaved BFloat16              | BF1CVTL, BF2CVTL              |
| BFCVT            | Multi-vector floating-point convert from BFloat16 to packed 8-bit floating-point format              | BFCVT                         |
| F1CVT, F2CVT     | Multi-vector floating-point convert from 8-bit floating-point to half-precision (in-order)           | F1CVT, F2CVT                  |
| F1CVTL, F2CVTL   | Multi-vector floating-point convert from 8-bit floating-point to deinterleaved half-precision        | F1CVTL, F2CVTL                |
| FCVT             | Multi-vector floating-point convert from half-precision to packed 8-bit floating-point format        | FCVT (narrowing, FP16 to FP8) |
| FCVT             | Multi-vector floating-point convert from single-precision to packed 8-bit floating-point format      | FCVT (narrowing, FP32 to FP8) |
| FCVTN            | Multi-vector floating-point convert from single-precision to interleaved 8-bit floating-point format | FCVTN (FP32 to FP8)           |

## C3.11.6 Floating-point round

Round each element of the source vectors to an integral floating-point value and place the results in the corresponding elements of the destination vectors.

## Table C3-256 SME2 Floating-point round to integral value instructions

| Mnemonic   | Instruction                                                                              | See    |
|------------|------------------------------------------------------------------------------------------|--------|
| FRINTA     | Multi-vector floating-point round to integral value, to nearest with ties away from zero | FRINTA |
| FRINTM     | Multi-vector floating-point round to integral value, toward minus Infinity               | FRINTM |
| FRINTN     | Multi-vector floating-point round to integral value, to nearest with ties to even        | FRINTN |
| FRINTP     | Multi-vector floating-point round to integral value, toward plus Infinity                | FRINTP |

## C3.11.7 Floating-point adjust exponent

## C3.11.7.1 Floating-point scaling

The FSCALE instructions perform floating-point scaling by integer powers of two.

## Table C3-257 SME2 floating-point scaling instructions

| Mnemonic   | Instruction                                 | See                                 |
|------------|---------------------------------------------|-------------------------------------|
| FSCALE     | Multi-vector floating-point adjust exponent | FSCALE (multiple and single vector) |
| FSCALE     | Multi-vector floating-point adjust exponent | FSCALE (multiple vectors)           |

## C3.11.7.2 BFloat16 scaling

The BFSCALE instructions perform BFloat16 scaling by integer powers of two.

## Table C3-258 SME2 BFloat16 scaling instructions

| Mnemonic   | Instruction                           | See                                  |
|------------|---------------------------------------|--------------------------------------|
| BFSCALE    | Multi-vector BFloat16 adjust exponent | BFSCALE (multiple and single vector) |
| BFSCALE    | Multi-vector BFloat16 adjust exponent | BFSCALE (multiple vectors)           |

## C3.11.8 Lookup table

Copy elements from ZT0 to the destination vectors using packed indices from a portion of the source vector.

## Table C3-259 SME2/SME2.1 Lookup table read instructions

| Mnemonic   | Instruction                           | See                                                                                                       |
|------------|---------------------------------------|-----------------------------------------------------------------------------------------------------------|
| LUTI2      | Lookup table read using 2-bit indexes | LUTI2 (four registers)                                                                                    |
| LUTI4      | Lookup table read using 4-bit indexes | LUTI4 (four registers, 16-bit &32-bit) LUTI4 (single) LUTI4 (two registers) LUTI4 (four registers, 8-bit) |

## C3.11.9 Move operations

Move between ZA single-vector groups, vector registers, or individual horizontal or vertical ZA tile slices.

## Table C3-260 SME/SME2 Move instructions

| Mnemonic   | Instruction                                               | See                                   |
|------------|-----------------------------------------------------------|---------------------------------------|
| MOVA       | Move four ZAsingle-vector groups to four vector registers | MOVA(array to vector, four registers) |
|            | Move two ZAsingle-vector groups to two vector registers   | MOVA(array to vector, two registers)  |

| Mnemonic   | Instruction                                               | See                                   |
|------------|-----------------------------------------------------------|---------------------------------------|
|            | Move four ZAtile slices to four vector registers          | MOVA(tile to vector, four registers)  |
|            | Move ZAtile slice to vector register                      | MOVA(tile to vector, single)          |
|            | Move two ZAtile slices to two vector registers            | MOVA(tile to vector, two registers)   |
|            | Move four vector registers to four ZAsingle-vector groups | MOVA(vector to array, four registers) |
|            | Move two vector registers to two ZAsingle-vector groups   | MOVA(vector to array, two registers)  |
|            | Move four vector registers to four ZAtile slices          | MOVA(vector to tile, four registers)  |
|            | Move vector register to ZAtile slice                      | MOVA(vector to tile, single)          |
|            | Move two vector registers to two ZAtile slices            | MOVA(vector to tile, two registers)   |

## C3.11.9.1 Lookup table move

Move 8 bytes between the ZT0 register and a general-purpose register at a specified byte offset.

MOVT (vector to table) copies the source vector register to ZT0 at a specified vector length offset.

## Table C3-261 SME2 Lookup table move instructions

| Mnemonic   | Instruction                                       | See                   |
|------------|---------------------------------------------------|-----------------------|
| MOVT       | Move 8 bytes from general-purpose register to ZT0 | MOVT(scalar to table) |
|            | Move 8 bytes from ZT0 to general-purpose register | MOVT(table to scalar) |
|            | Move vector register to ZT0                       | MOVT(vector to table) |

## C3.11.9.2 Move and zero

Move contents of ZA single-vector groups or of consecutive horizontal or vertical slices within a ZA tile to the destination vectors and zero the source contents.

## Table C3-262 SME2.1 Move and zero instructions

| Mnemonic   | Instruction                                                   | See                                    |
|------------|---------------------------------------------------------------|----------------------------------------|
| MOVAZ      | Move and zero four ZAsingle-vector groups to vector registers | MOVAZ(array to vector, four registers) |
| MOVAZ      | Move and zero two ZAsingle-vector groups to vector registers  | MOVAZ(array to vector, two registers)  |
| MOVAZ      | Move and zero four ZAtile slices to vector registers          | MOVAZ(tile to vector, four registers)  |
| MOVAZ      | Move and zero ZAtile slice to vector register                 | MOVAZ(tile to vector, single)          |
| MOVAZ      | Move and zero two ZAtile slices to vector registers           | MOVAZ(tile to vector, two registers)   |

## C3.11.10 Multi-vector arithmetic

## C3.11.10.1 Add and subtract

Add or subtract vectors from ZA single-vector groups or destructively place results in corresponding elements of the source vectors.

## Table C3-263 SME2 Add and subtract instructions

| Mnemonic   | Instruction                                                                     | See                                             |
|------------|---------------------------------------------------------------------------------|-------------------------------------------------|
| ADD        | Add multi-vector to ZAarray vector accumulators                                 | ADD(array accumulators)                         |
| ADD        | Add replicated single vector to multi-vector with ZAarray vector results        | ADD(array results, multiple and single vector)  |
| ADD        | Add multi-vector to multi-vector with ZAarray vector results                    | ADD(array results, multiple vectors)            |
| ADD        | Add replicated single vector to multi-vector with multi-vector result           | ADD(to vector)                                  |
| SUB        | Subtract multi-vector from ZAarray vector accumulators                          | SUB (array accumulators)                        |
| SUB        | Subtract replicated single vector from multi-vector with ZAarray vector results | SUB (array results, multiple and single vector) |
| SUB        | Subtract multi-vector from multi-vector with ZAarray vector results             | SUB (array results, multiple vectors)           |

## C3.11.10.2 Add vector to array

Add each element of the source vector to the corresponding Active element of each vertical or horizontal slice of a ZA tile.

## Table C3-264 SME Add vector to array instructions

| Mnemonic   | Instruction                                | See   |
|------------|--------------------------------------------|-------|
| ADDHA      | Add horizontally vector elements to ZAtile | ADDHA |
| ADDVA      | Add vertically vector elements to ZAtile   | ADDVA |

## C3.11.10.3 Floating-point add and subtract

Destructively add or subtract all elements of the source vectors from the corresponding elements of the ZA single-vector groups.

## Table C3-265 SME2 Floating-point add and subtract instructions

| Mnemonic   | Instruction                                                                    | See   |
|------------|--------------------------------------------------------------------------------|-------|
| BFADD      | BFloat16 floating-point add multi-vector to ZAarray vector accumulators        | BFADD |
| BFSUB      | BFloat16 floating-point subtract multi-vector from ZAarray vector accumulators | BFSUB |
| FADD       | Floating-point add multi-vector to ZAarray vector accumulators                 | FADD  |
| FSUB       | Floating-point subtract multi-vector from ZAarray vector accumulators          | FSUB  |

## C3.11.11 Multi-vector minimum/maximum

Determine the minimum or maximum of elements of the second source vector and the corresponding elements of the first source vectors and destructively place the results in the corresponding elements of the first source vectors.

## C3.11.11.1 BFloat16 minimum/maximum

These instructions follow the SME2.1 non-widening BFloat16 numerical behaviors corresponding to instructions that place their results in two or four SVE Z vectors. If FEAT\_SVE\_B16B16 is implemented, these instructions are also implemented.

## Table C3-266 SME2.1 BFloat16 minimum/maximum

| Mnemonic   | Instruction                                                   | See                                 |
|------------|---------------------------------------------------------------|-------------------------------------|
| BFMAX      | Multi-vector BFloat16 floating-point maximum by vector        | BFMAX(multiple and single vector)   |
|            | Multi-vector BFloat16 floating-point maximum                  | BFMAX(multiple vectors)             |
| BFMAXNM    | Multi-vector BFloat16 floating-point maximum number by vector | BFMAXNM(multiple and single vector) |
|            | Multi-vector BFloat16 floating-point maximum number           | BFMAXNM(multiple vectors)           |
| BFMIN      | Multi-vector BFloat16 floating-point minimum by vector        | BFMIN (multiple and single vector)  |
|            | Multi-vector BFloat16 floating-point minimum                  | BFMIN (multiple vectors)            |
| BFMINNM    | Multi-vector BFloat16 floating-point minimum number by vector | BFMINNM(multiple and single vector) |
|            | Multi-vector BFloat16 floating-point minimum number           | BFMINNM(multiple vectors)           |

## C3.11.11.2 Floating-point minimum/maximum

## Table C3-267 SME2 Floating-point minimum/maximum

| Mnemonic   | Instruction                                          | See                                 |
|------------|------------------------------------------------------|-------------------------------------|
| FMAX       | Multi-vector floating-point maximum by vector        | FMAX(multiple and single vector)    |
|            | Multi-vector floating-point maximum                  | FMAX(multiple vectors)              |
| FMAXNM     | Multi-vector floating-point maximum number by vector | FMAXNM(multiple and single vector)  |
|            | Multi-vector floating-point maximum number           | FMAXNM(multiple vectors)            |
| FMIN       | Multi-vector floating-point minimum by vector        | FMIN (multiple and single vector)   |
|            | Multi-vector floating-point minimum                  | FMIN (multiple vectors)             |
| FMINNM     | Multi-vector floating-point minimum number by vector | FMINNM(multiple and single vectors) |
|            | Multi-vector floating-point minimum number           | FMINNM(multiple vectors)            |

## C3.11.11.3 Floating-point minimum/maximum absolute value

## Table C3-268 SME2 Floating-point absolute minimum/maximum

| Mnemonic   | Instruction                                  | See   |
|------------|----------------------------------------------|-------|
| FAMAX      | Multi-vector floating-point absolute maximum | FAMAX |
| FAMIN      | Multi-vector floating-point absolute minimum | FAMIN |

## C3.11.11.4 Integer minimum/maximum

## Table C3-269 SME2 Integer minimum/maximum

| Mnemonic   | Instruction                             | See                               |
|------------|-----------------------------------------|-----------------------------------|
| SMAX       | Multi-vector signed maximum by vector   | SMAX(multiple and single vector)  |
|            | Multi-vector signed maximum             | SMAX(multiple vectors)            |
| SMIN       | Multi-vector signed minimum by vector   | SMIN (multiple and single vector) |
|            | Multi-vector signed minimum             | SMIN (multiple vectors)           |
| UMAX       | Multi-vector unsigned maximum by vector | UMAX(multiple and single vector)  |
|            | Multi-vector unsigned maximum           | UMAX(multiple vectors)            |
| UMIN       | Multi-vector unsigned minimum by vector | UMIN(multiple and single vector)  |
|            | Multi-vector unsigned minimum           | UMIN(multiple vectors)            |

## C3.11.12 Multi-vector multiply

Multiply the floating-point elements of the first source vectors with the corresponding elements of the second source vectors and place the results in the corresponding elements of the destination vectors.

## C3.11.12.1 BFloat16 multi-vector multiply

## Table C3-270 SME2.2 BFloat16 multi-vector multiply instructions

| Mnemonic   | Instruction                              | See                               |
|------------|------------------------------------------|-----------------------------------|
| BFMUL      | Multi-vector BFloat16 multiply by vector | BFMUL(multiple and single vector) |
| BFMUL      | Multi-vector BFloat16 multiply           | BFMUL(multiple vectors)           |

## C3.11.12.2 Floating-point multi-vector multiply

## Table C3-271 SME2.2 Floating-point multi-vector multiply instructions

| Mnemonic   | Instruction                                    | See                              |
|------------|------------------------------------------------|----------------------------------|
| FMUL       | Multi-vector floating-point multiply by vector | FMUL(multiple and single vector) |
|            | Multi-vector floating-point multiply           | FMUL(multiple vectors)           |

## C3.11.13 Multi-vector multiply-accumulate

Multiply the corresponding elements of the first source vectors by the corresponding elements of the second source vector and destructively, without intermediate rounding, add to or subtract from the corresponding elements of the ZA single-vector groups.

## C3.11.13.1 BFloat16 multiply-accumulate

## Table C3-272 SME2 BFloat16 multiply-accumulate instructions

| Mnemonic   | Instruction                                                                     | See                                  |
|------------|---------------------------------------------------------------------------------|--------------------------------------|
| BFMLA      | Multi-vector BFloat16 floating-point fused multiply-add by indexed element      | BFMLA(multiple and indexed vector)   |
| BFMLA      | Multi-vector BFloat16 floating-point fused multiply-add by vector               | BFMLA(multiple and single vector)    |
| BFMLA      | Multi-vector BFloat16 floating-point fused multiply-add                         | BFMLA(multiple vectors)              |
| BFMLAL     | Multi-vector BFloat16 floating-point multiply-add long by indexed element       | BFMLAL(multiple and indexed vector)  |
| BFMLAL     | Multi-vector BFloat16 floating-point multiply-add long by vector                | BFMLAL(multiple and single vector)   |
| BFMLAL     | Multi-vector BFloat16 floating-point multiply-add long                          | BFMLAL(multiple vectors)             |
| BFMLS      | Multi-vector BFloat16 floating-point fused multiply-subtract by indexed element | BFMLS (multiple and indexed vector)  |
| BFMLS      | Multi-vector BFloat16 floating-point fused multiply-subtract by vector          | BFMLS (multiple and single vector)   |
| BFMLS      | Multi-vector BFloat16 floating-point fused multiply-subtract                    | BFMLS (multiple vectors)             |
| BFMLSL     | Multi-vector BFloat16 floating-point multiply-subtract long by indexed element  | BFMLSL (multiple and indexed vector) |
| BFMLSL     | Multi-vector BFloat16 floating-point multiply-subtract long by vector           | BFMLSL (multiple and single vector)  |
| BFMLSL     | Multi-vector BFloat16 floating-point multiply-subtract long                     | BFMLSL (multiple vectors)            |

## C3.11.13.2 Floating-point multiply-accumulate

## Table C3-273 SME2 Floating-point multi-vector multiply-accumulate instructions

| Mnemonic   | Instruction                                                            | See                                 |
|------------|------------------------------------------------------------------------|-------------------------------------|
| FMLA       | Multi-vector floating-point fused multiply-add by indexed element      | FMLA(multiple and indexed vector)   |
| FMLA       | Multi-vector floating-point fused multiply-add by vector               | FMLA(multiple and single vector)    |
| FMLA       | Multi-vector floating-point fused multiply-add                         | FMLA(multiple vectors)              |
| FMLAL      | Multi-vector floating-point multiply-add long by indexed element       | FMLAL(multiple and indexed vector)  |
| FMLAL      | Multi-vector floating-point multiply-add long by vector                | FMLAL(multiple and single vector)   |
| FMLAL      | Multi-vector floating-point fused multiply-add long                    | FMLAL(multiple vectors)             |
| FMLS       | Multi-vector floating-point fused multiply-subtract by indexed element | FMLS (multiple and indexed vector)  |
| FMLS       | Multi-vector floating-point fused multiply-subtract by vector          | FMLS (multiple and single vector)   |
| FMLS       | Multi-vector floating-point fused multiply-subtract                    | FMLS (multiple vectors)             |
| FMLSL      | Multi-vector floating-point multiply-subtract long by indexed element  | FMLSL (multiple and indexed vector) |
| FMLSL      | Multi-vector floating-point multiply-subtract long by vector           | FMLSL (multiple and single vector)  |
| FMLSL      | Multi-vector floating-point multiply-subtract long                     | FMLSL (multiple vectors)            |

## C3.11.13.3 FP8 floating-point widening multiply-accumulate

The FP8 floating-point multiply-accumulate instructions widen the 8-bit floating-point elements in the source vectors to half-precision or single-precision format and multiply the corresponding elements.

They generate a fused, downscaled product and accumulate into the corresponding elements of the destination vector, without intermediate rounding.

For these instructions, the unbounded intermediate product is scaled by subtracting the value specified in FPMR.LSCALE from its unbounded exponent. For more information, see the instruction descriptions.

## Table C3-274 SME2 FP8 floating-point widening multiply-accumulate instructions

| Mnemonic   | Instruction                                                                                     | See                                             |
|------------|-------------------------------------------------------------------------------------------------|-------------------------------------------------|
| FMLAL      | Multi-vector 8-bit floating-point multiply-add long by indexed element to half-precision        | FMLAL(multiple and indexed vector, FP8 to FP16) |
| FMLAL      | Multi-vector 8-bit floating-point multiply-add long by vector to half-precision                 | FMLAL(multiple and single vector, FP8 to FP16)  |
| FMLAL      | Multi-vector 8-bit floating-point multiply-add long to half-precision                           | FMLAL(multiple vectors, FP8 to FP16)            |
| FMLALL     | Multi-vector 8-bit floating-point multiply-add long-long by indexed element to single-precision | FMLALL(multiple and indexed vector)             |
| FMLALL     | Multi-vector 8-bit floating-point multiply-add long-long by vector to single-precision          | FMLALL(multiple and single vector)              |
| FMLALL     | Multi-vector 8-bit floating-point multiply-add long-long to single-precision                    | FMLALL(multiple vectors)                        |

## C3.11.13.4 Integer multiply-accumulate

## Table C3-275 SME2 Integer multi-vector multiply-accumulate instructions

| Mnemonic   | Instruction                                                                       | See                                  |
|------------|-----------------------------------------------------------------------------------|--------------------------------------|
| SMLAL      | Multi-vector signed integer multiply-add long by indexed element                  | SMLAL(multiple and indexed vector)   |
| SMLAL      | Multi-vector signed integer multiply-add long by vector                           | SMLAL(multiple and single vector)    |
| SMLAL      | Multi-vector signed integer multiply-add long                                     | SMLAL(multiple vectors)              |
| SMLALL     | Multi-vector signed integer multiply-add long-long by indexed element             | SMLALL(multiple and indexed vector)  |
| SMLALL     | Multi-vector signed integer multiply-add long-long by vector                      | SMLALL(multiple and single vector)   |
| SMLALL     | Multi-vector signed integer multiply-add long-long                                | SMLALL(multiple vectors)             |
| SMLSL      | Multi-vector signed integer multiply-subtract long by indexed element             | SMLSL (multiple and indexed vector)  |
| SMLSL      | Multi-vector signed integer multiply-subtract long by vector                      | SMLSL (multiple and single vector)   |
| SMLSL      | Multi-vector signed integer multiply-subtract long                                | SMLSL (multiple vectors)             |
| SMLSLL     | Multi-vector signed integer multiply-subtract long-long by indexed element        | SMLSLL (multiple and indexed vector) |
| SMLSLL     | Multi-vector signed integer multiply-subtract long-long by vector                 | SMLSLL (multiple and single vector)  |
| SMLSLL     | Multi-vector signed integer multiply-subtract long-long                           | SMLSLL (multiple vectors)            |
| SUMLALL    | Multi-vector signed by unsigned integer multiply-add long-long by indexed element | SUMLALL(multiple and indexed vector) |
| SUMLALL    | Multi-vector signed by unsigned integer multiply-add long-long by vector          | SUMLALL(multiple and single vector)  |

| Mnemonic   | Instruction                                                                       | See                                  |
|------------|-----------------------------------------------------------------------------------|--------------------------------------|
| UMLAL      | Multi-vector unsigned integer multiply-add long by indexed element                | UMLAL(multiple and indexed vector)   |
| UMLAL      | Multi-vector unsigned integer multiply-add long by vector                         | UMLAL(multiple and single vector)    |
| UMLAL      | Multi-vector unsigned integer multiply-add long                                   | UMLAL(multiple vectors)              |
| UMLALL     | Multi-vector unsigned integer multiply-add long-long by indexed element           | UMLALL(multiple and indexed vector)  |
| UMLALL     | Multi-vector unsigned integer multiply-add long-long by vector                    | UMLALL(multiple and single vector)   |
| UMLALL     | Multi-vector unsigned integer multiply-add long-long                              | UMLALL(multiple vectors)             |
| UMLSL      | Multi-vector unsigned integer multiply-subtract long by indexed element           | UMLSL(multiple and indexed vector)   |
| UMLSL      | Multi-vector unsigned integer multiply-subtract long by vector                    | UMLSL(multiple and single vector)    |
| UMLSL      | Multi-vector unsigned integer multiply-subtract long by indexed element           | UMLSL(multiple vectors)              |
| UMLSLL     | Multi-vector unsigned integer multiply-subtract long-long by indexed element      | UMLSLL(multiple and indexed vector)  |
| UMLSLL     | Multi-vector unsigned integer multiply-subtract long-long by vector               | UMLSLL(multiple and single vector)   |
| UMLSLL     | Multi-vector unsigned integer multiply-subtract long-long                         | UMLSLL(multiple vectors)             |
| USMLALL    | Multi-vector unsigned by signed integer multiply-add long-long by indexed element | USMLALL(multiple and indexed vector) |
| USMLALL    | Multi-vector unsigned by signed integer multiply-add long-long by vector          | USMLALL(multiple and single vector)  |
| USMLALL    | Multi-vector unsigned by signed integer multiply-add long-long                    | USMLALL(multiple vectors)            |

## C3.11.14 Multi-vector multiply high

These instructions multiply then double the corresponding elements of the first and second source vectors and destructively place the most significant half of the result in the corresponding elements of the first and second source vectors.

## Table C3-276 SME2 Multi-vector multiply high

| Mnemonic   | Instruction                                                     | See                                 |
|------------|-----------------------------------------------------------------|-------------------------------------|
| SQDMULH    | Multi-vector signed saturating doubling multiply high by vector | SQDMULH(multiple and single vector) |
| SQDMULH    | Multi-vector signed saturating doubling multiply high           | SQDMULH(multiple vectors)           |

## C3.11.15 Multi-vector select

Copy into elements of the destination vectors the corresponding elements from the first source vectors where the corresponding predicate elements are TRUE, and from the second source vectors where the corresponding predicate elements are FALSE.

| Mnemonic   | Instruction                                                 | See   |
|------------|-------------------------------------------------------------|-------|
| SEL        | Multi-vector conditionally select elements from two vectors | SEL   |

## C3.11.16 Multi-vector shift and convert

Convert or shift the value of each element of the source vectors and place the results in the corresponding destination vector elements.

## Table C3-278 SME2 Multi-vector shift and convert instructions

| Mnemonic   | Instruction                                                                                     | See                                              |
|------------|-------------------------------------------------------------------------------------------------|--------------------------------------------------|
| SCVTF      | Multi-vector signed integer convert to floating-point                                           | SCVTF                                            |
| SQCVT      | Multi-vector signed saturating extract narrow                                                   | SQCVT (four registers) SQCVT (two registers)     |
| SQCVTN     | Multi-vector signed saturating extract narrow and interleave                                    | SQCVTN                                           |
| SQCVTU     | Multi-vector signed saturating unsigned extract narrow                                          | SQCVTU(four registers) SQCVTU(two registers)     |
| SQCVTUN    | Multi-vector signed saturating unsigned extract narrow and interleave                           | SQCVTUN                                          |
| SQRSHR     | Multi-vector signed saturating rounding shift right narrow by immediate                         | SQRSHR (four registers) SQRSHR (two registers)   |
| SQRSHRN    | Multi-vector signed saturating rounding shift right narrow by immediate and interleave          | SQRSHRN                                          |
| SQRSHRU    | Multi-vector signed saturating rounding shift right unsigned narrow by immediate                | SQRSHRU (four registers) SQRSHRU (two registers) |
| SQRSHRUN   | Multi-vector signed saturating rounding shift right unsigned narrow by immediate and interleave | SQRSHRUN                                         |
| SRSHL      | Multi-vector signed rounding shift left by vector                                               | SRSHL (multiple and single vector)               |
| SRSHL      | Multi-vector signed rounding shift left                                                         | SRSHL (multiple vectors)                         |
| UCVTF      | Multi-vector unsigned integer convert to floating-point                                         | UCVTF                                            |
| UQCVT      | Multi-vector unsigned saturating extract narrow                                                 | UQCVT(four registers) UQCVT(two registers)       |
| UQCVTN     | Multi-vector unsigned saturating extract narrow and interleave                                  | UQCVTN                                           |
| UQRSHR     | Multi-vector unsigned saturating rounding shift right narrow by immediate                       | UQRSHR(four registers) UQRSHR(two registers)     |
| UQRSHRN    | Multi-vector unsigned saturating rounding shift right narrow by immediate and interleave        | UQRSHRN                                          |
| URSHL      | Multi-vector unsigned rounding shift left by vector                                             | URSHL (multiple and single vector)               |
| URSHL      | Multi-vector unsigned rounding shift left                                                       | URSHL (multiple vectors)                         |

## C3.11.17 Outer product

Multiply, or widen and multiply, the sub-matrix in the first source vector by the sub-matrix in the second source vector and add or subtract from the destination tile.

## C3.11.17.1 BFloat16 outer product

## Table C3-279 SME BFloat16 outer product instructions

| Mnemonic   | Instruction                                          | See                   |
|------------|------------------------------------------------------|-----------------------|
| BFMOPA     | BFloat16 floating-point outer product and accumulate | BFMOPA(non-widening)  |
|            | BFloat16 sum of outer products and accumulate        | BFMOPA(widening)      |
| BFMOPS     | BFloat16 floating-point outer product and subtract   | BFMOPS (non-widening) |
|            | BFloat16 sum of outer products and subtract          | BFMOPS (widening)     |

## C3.11.17.2 Binary outer product

## Table C3-280 SME2 Binary outer product instructions

| Mnemonic   | Instruction                                                        | See   |
|------------|--------------------------------------------------------------------|-------|
| BMOPA      | Bitwise exclusive NORpopulation count outer product and accumulate | BMOPA |
| BMOPS      | Bitwise exclusive NORpopulation count outer product and subtract   | BMOPS |

## C3.11.17.3 Floating-point outer product

## Table C3-281 SME Floating-point outer product instructions

| Mnemonic   | Instruction                                                        | See                  |
|------------|--------------------------------------------------------------------|----------------------|
| FMOPA      | Floating-point outer product and accumulate                        | FMOPA(non-widening)  |
|            | Half-precision floating-point sum of outer products and accumulate | FMOPA(widening)      |
| FMOPS      | Floating-point outer product and subtract                          | FMOPS (non-widening) |
|            | Half-precision floating-point sum of outer products and subtract   | FMOPS (widening)     |

## C3.11.17.4 FP8 floating-point outer product

For FP8 outer product instructions, the unbounded intermediate sum of outer products is scaled by subtracting the value specified in FPMR.LSCALE from its unbounded exponent. For more information, see the instruction descriptions.

## Table C3-282 SME2 FP8 floating-point outer product instructions

| Mnemonic Instruction   | Mnemonic Instruction                                      | See                                 |
|------------------------|-----------------------------------------------------------|-------------------------------------|
| FMOPA                  | 8-bit floating-point sum of outer products and accumulate | FMOPA(widening, 2-way, FP8 to FP16) |

## C3.11.17.5 Integer outer product

## Table C3-283 SME Integer outer product instructions

| Mnemonic   | Instruction                                                     | See                         |
|------------|-----------------------------------------------------------------|-----------------------------|
| SMOPA      | Signed integer sum of outer products and accumulate             | SMOPA(2-way) SMOPA(4-way)   |
| SMOPS      | Signed integer sum of outer products and subtract               | SMOPS (2-way) SMOPS (4-way) |
| SUMOPA     | Signed by unsigned integer sum of outer products and accumulate | SUMOPA                      |
| SUMOPS     | Signed by unsigned integer sum of outer products and subtract   | SUMOPS                      |
| UMOPA      | Unsigned integer sum of outer products and accumulate           | UMOPA(2-way) UMOPA(4-way)   |
| UMOPS      | Unsigned integer sum of outer products and subtract             | UMOPS(2-way) UMOPS(4-way)   |
| USMOPA     | Unsigned by signed integer sum of outer products and accumulate | USMOPA                      |
| USMOPS     | Unsigned by signed integer sum of outer products and subtract   | USMOPS                      |

## C3.11.18 Quarter-tile outer product

The quarter-tile outer product instructions generate four independent quarter-tile outer products from the sub-matrices in the half-vectors of the one or two first and second source vectors. The resulting quarter-tile outer products are added to or subtracted from the destination ZA tile.

## C3.11.18.1 BFloat16 quarter-tile outer product

## Table C3-284 SME BFloat16 quarter-tile outer product instructions

| Mnemonic   | Instruction                                                    | See                    |
|------------|----------------------------------------------------------------|------------------------|
| BFMOP4A    | BFloat16 quarter-tile outer products, accumulating             | BFMOP4A (non-widening) |
|            | BFloat16 quarter-tile sums of two outer products, accumulating | BFMOP4A (widening)     |
| BFMOP4S    | BFloat16 quarter-tile outer products, subtracting              | BFMOP4S (non-widening) |
|            | BFloat16 quarter-tile sums of two outer products, subtracting  | BFMOP4S (widening)     |

## C3.11.18.2 Floating-point quarter-tile outer product

## Table C3-285 SME floating-point quarter-tile outer product instructions

| Mnemonic   | Instruction                                                          | See                                    |
|------------|----------------------------------------------------------------------|----------------------------------------|
| FMOP4A     | Floating-point quarter-tile outer products, accumulating             | FMOP4A (non-widening)                  |
|            | Half-precision quarter-tile sums of two outer products, accumulating | FMOP4A (widening, 2-way, FP16 to FP32) |
| FMOP4S     | Floating-point quarter-tile outer products, subtracting              | FMOP4S (non-widening)                  |
|            | Half-precision quarter-tile sums of two outer products, subtracting  | FMOP4S (widening)                      |

## C3.11.18.3 FP8 floating-point quarter-tile outer product

## Table C3-286 SME2 FP8 floating-point quarter-tile outer product instructions

| Mnemonic Instruction   | Mnemonic Instruction                                                        | See                                   |
|------------------------|-----------------------------------------------------------------------------|---------------------------------------|
| FMOP4A                 | 8-bit floating-point quarter-tile sums of two outer products, accumulating  | FMOP4A (widening, 2-way, FP8 to FP16) |
|                        | 8-bit floating-point quarter-tile sums of four outer products, accumulating | FMOP4A (widening, 4-way)              |

## C3.11.18.4 Integer quarter-tile outer product

## Table C3-287 SME Integer quarter-tile outer product instructions

| Mnemonic   | Instruction                                                                       | See            |
|------------|-----------------------------------------------------------------------------------|----------------|
| SMOP4A     | Signed integer quarter-tile sums of two outer products, accumulating              | SMOP4A (2-way) |
| SMOP4A     | Signed integer quarter-tile sums of four outer products, accumulating             | SMOP4A (4-way) |
| SMOP4S     | Signed integer quarter-tile sums of two outer products, subtracting               | SMOP4S (2-way) |
| SMOP4S     | Signed integer quarter-tile sums of four outer products, subtracting              | SMOP4S (4-way) |
| SUMOP4A    | Signed by unsigned integer quarter-tile sums of four outer products, accumulating | SUMOP4A        |
| SUMOP4S    | Signed by unsigned integer quarter-tile sums of four outer products, subtracting  | SUMOP4S        |
| UMOP4A     | Unsigned integer quarter-tile sums of two outer products, accumulating            | UMOP4A(2-way)  |
| UMOP4A     | Unsigned integer quarter-tile sums of four outer products, accumulating           | UMOP4A(4-way)  |
| UMOP4S     | Unsigned integer quarter-tile sums of two outer products, subtracting             | UMOP4S (2-way) |
| UMOP4S     | Unsigned integer quarter-tile sums of four outer products, subtracting            | UMOP4S (4-way) |
| USMOP4A    | Unsigned by signed integer quarter-tile sums of four outer products, accumulating | USMOP4A        |

| Mnemonic   | Instruction                                                                      | See     |
|------------|----------------------------------------------------------------------------------|---------|
| USMOP4S    | Unsigned by signed integer quarter-tile sums of four outer products, subtracting | USMOP4S |

## C3.11.19 Structured sparsity outer product

The SME structured sparsity outer product instructions accumulate the products or sum-of-products of all elements of the second source vector and selected elements of the first source vectors.

The SME widening structured sparsity outer product instructions widen and multiply a dense matrix by a 2:4 sparse matrix and accumulate to the destination tile. In a 2:4 structured sparsity pattern, two elements are selected per group of four elements, discarding the remaining two elements.

The SME non-widening structured sparsity outer product instructions multiply a dense matrix by a 1:2 sparse matrix and accumulate to the destination tile. In a 1:2 structured sparsity pattern, one element is selected out of a pair of elements, discarding the remaining element.

## C3.11.19.1 BFloat16 sparsity outer product

## Table C3-288 SME BFloat16 sparsity outer product instructions

| Mnemonic   | Instruction                                             | See                    |
|------------|---------------------------------------------------------|------------------------|
| BFTMOPA    | BFloat16 sparse outer product, accumulating             | BFTMOPA (non-widening) |
| BFTMOPA    | BFloat16 sparse sum of two outer products, accumulating | BFTMOPA (widening)     |

## C3.11.19.2 Floating-point sparsity outer product

## Table C3-289 SME Floating-point sparsity outer product instructions

| Mnemonic   | Instruction                                                   | See                                    |
|------------|---------------------------------------------------------------|----------------------------------------|
| FTMOPA     | Floating-point sparse outer product, accumulating             | FTMOPA (non-widening)                  |
|            | Half-precision sparse sum of two outer products, accumulating | FTMOPA (widening, 2-way, FP16 to FP32) |

## C3.11.19.3 FP8 floating-point sparsity outer product

## Table C3-290 SME2 FP8 floating-point sparsity outer product instructions

| Mnemonic Instruction   | Mnemonic Instruction                                                 | See                                   |
|------------------------|----------------------------------------------------------------------|---------------------------------------|
| FTMOPA                 | 8-bit floating-point sparse sum of two outer products, accumulating  | FTMOPA (widening, 2-way, FP8 to FP16) |
|                        | 8-bit floating-point sparse sum of four outer products, accumulating | FTMOPA (widening, 4-way)              |

## C3.11.19.4 Integer sparsity outer product

## Table C3-291 SME Integer sparsity outer product instructions

| Mnemonic   | Instruction                                                                | See            |
|------------|----------------------------------------------------------------------------|----------------|
| STMOPA     | Signed integer sparse sum of two outer products, accumulating              | STMOPA (2-way) |
|            | Signed integer sparse sum of four outer products, accumulating             | STMOPA (4-way) |
| SUTMOPA    | Signed by unsigned integer sparse sum of four outer products, accumulating | SUTMOPA        |
| USTMOPA    | Unsigned by signed integer sparse sum of four outer products, accumulating | USTMOPA        |
| UTMOPA     | Unsigned integer sparse sum of two outer products, accumulating            | UTMOPA(2-way)  |
|            | Unsigned integer sparse sum of four outer products, accumulating           | UTMOPA(4-way)  |

## C3.11.20 Stack frame operations

Multiply the Streaming SVE vector register size in bytes by an immediate and add the result to the destination general-purpose register or current stack pointer. RDSVL only places the result in the destination general-purpose register without addition.

## Table C3-292 SME Stack frame instructions

| Mnemonic   | Instruction                                                              | See    |
|------------|--------------------------------------------------------------------------|--------|
| ADDSPL     | Add multiple of Streaming SVE predicate register size to scalar register | ADDSPL |
| ADDSVL     | Add multiple of Streaming SVE vector register size to scalar register    | ADDSVL |
| RDSVL      | Read multiple of Streaming SVE vector register size to scalar register   | RDSVL  |

## C3.11.21 Unpack and extend

Unpack elements from the source vectors and extend them to place in elements of twice their size within the destination vectors.

## Table C3-293 SME2 Unpack and extend instructions

| Mnemonic   | Instruction                                  | See   |
|------------|----------------------------------------------|-------|
| SUNPK      | Unpack and sign-extend multi-vector elements | SUNPK |
| UUNPK      | Unpack and zero-extend multi-vector elements | UUNPK |

## C3.11.22 Zero operations

Set all corresponding bytes or ZA vector groups to zero.

## Table C3-294 SME/SME2 Zero instructions

| Mnemonic   | Instruction                           | See          |
|------------|---------------------------------------|--------------|
| ZERO       | Zero ZT0                              | ZERO (table) |
|            | Zero a list of 64-bit element ZAtiles | ZERO (tiles) |

## C3.11.22.1 Zero ZA array vectors

## Table C3-295 SME2.1 Zero ZA array vectors instructions

| Mnemonic   | Instruction                 | See                  |
|------------|-----------------------------|----------------------|
| ZERO       | Zero ZAdouble-vector groups | ZERO (double-vector) |
|            | Zero ZAquad-vector groups   | ZERO (quad-vector)   |
|            | Zero ZAsingle-vector groups | ZERO (single-vector) |

## Chapter C4 A64 Instruction Set Encoding

This chapter describes the encoding of the A64 instruction set. It contains the following section:

- A64 instruction set encoding.

In this chapter:

- In the decode tables, an entry of x for a field value means the value of the field does not affect the decoding.