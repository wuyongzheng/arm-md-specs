## B1.10 Command testing

IMBNZM

Command definitions can be used to generate testbenches which check whether an implementation complies with the specified failure and success conditions.

IJGGJN

A testbench for the EXAMPLE\_ADD command presented above would look similar to the following:

```
DRAFT // Test EXAMPLE_ADD command Test_ExampleAdd(Registers regs_in) // Unpack input values RmmPa params_ptr = regs_in.X1; // Evaluate context values ExampleParams params = ExampleParams(params_ptr); // Evaluate failure pre-conditions boolean params_align_pre = !AddrIsRmiGranuleAligned(params_ptr); // Execute command regs_out = RmiExampleAdd(regs_in); // Pack output values CommandReturnCode result = regs_out.X0; integer sum = regs_out.X1; integer zero = regs_out.X2; // Check return code boolean success = (result == Success); // Evaluate failure post-conditions boolean params_align_post = result == Status(ErrorInput, 1); boolean params_gpt_post = result == Status(ErrorInputMemory, 0); // Evaluate success conditions boolean sum_post = sum == params.x + params.y; boolean zero_post = zero == (params.x == 0) || (params.z == 0); // Check failure conditions, in order specified assert params_align_pre IMPLIES params_align_post; assert (!params_align_pre && params_gpt_pre) IMPLIES params_gpt_post; // Check that, if no failure pre-condition was violated, command succeeded assert (!params_align_pre && !params_gpt_pre) IMPLIES success; // Check success conditions, without any ordering assert success IMPLIES S01_post; assert success IMPLIES S02_post;
```

Note that the syntax x IMPLIES y , which is logically equivalent to !x || y , is not yet defined in ASL.