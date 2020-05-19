"""
Day 2: Add the ability to load files dynamically, get mult.ls8 running
 Un-hardcode the machine code
 Implement the load() function to load an .ls8 file given the filename passed in as an argument
 Implement a Multiply instruction (run mult.ls8)
"""
import sys

class CPU:
    """Main CPU class."""

    """Construct a new CPU."""
    def __init__(self):
        # RAM
        self.ram = [0] * 256
        # CPU registers
        self.reg = [0] * 8
        # Program counter
        self.pc = 0
        # Instruction register
        self.ir = 0
        # Memory address register
        # self.mar = 0
        # # Memory address register
        # self.mdr = 0
        # # Op codes (instructions)
        self.opcodes = {
            0b10000010: self.ldi,
            0b01000111: self.prn,
            0b00000001:self.hlt
        }

    ### CPU opcodes ###
    # hlt: Exit the executing program
    def hlt(self, mar, mdr):
        exit(0)
    # ldi: Load immediate = Load the data in mdr into the register specified in mar
    def ldi(self, mar, mdr):
        self.reg[mar] = mdr
        self.pc += 3
    # prn: print the value in the register specified in mar
    def prn(self, mar, mdr):
        print(self.reg[mar])
        self.pc += 2


    # Read the value stored in memory location adr
    def ram_read(self, mar):
        return self.ram[mar]

   # Write the value (mdr) the value stored in memory location adr
    def ram_write(self, mdr, mar):
        self.ram[mar] = mdr

    def load(self):
        """Load a program into memory."""

        

        # For now, we've just hardcoded a program:
        # RG0 = 0b00000000
        # RG1 = 0b00000001
        # RG2 = 0b00000010
        # RG3 = 0b00000011
        # RG4 = 0b00000100
        # RG5 = 0b00000101
        # RG6 = 0b00000110
        # RG7 = 0b00000111

        # program = [
        #     # From print8.ls8
        #     0b10000010, # LDI R0,8
        #     RG0,
        #     0b00001000,
        #     0b01000111, # PRN R0
        #     RG0,
        #     0b00000001, # HLT
        # ]

        # for instruction in program:
        #     self.ram[address] = instruction
        #     address += 1
        
        # Memory load pointer
        address = 0

        # Open and parsee the program file
        with open(sys.argv[1]) as program:
            for instruction in program:
                # print(f'instruction read = {instruction}')
                line_read = instruction.split("#")[0].strip()
                if line_read == '':
                    continue
                prog_step = int(line_read, 2)
                # print(prog_step)
                self.ram[address] = prog_step
                # print(f'ram[{address}] = {self.ram[address]}')
                address += 1

    """Run the CPU."""
    def run(self):
        while True:
            # Initialize the program
            self.ir = self.ram[self.pc]
            # Cache the first two values in memory
            op_a = self.ram[self.pc + 1]
            op_b = self.ram[self.pc + 2]

            # Execute the opcode in the opcode dict
            # print(self.opcodes[self.ir])
            self.opcodes[self.ir](op_a, op_b)


    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op == "ADD":
            self.reg[reg_a] += self.reg[reg_b]
        #elif op == "SUB": etc
        else:
            raise Exception("Unsupported ALU operation")

    def trace(self):
        """
        Handy function to print out the CPU state. You might want to call this
        from run() if you need help debugging.
        """

        print(f"TRACE: %02X | %02X %02X %02X |" % (
            self.pc,
            #self.fl,
            #self.ie,
            self.ram_read(self.pc),
            self.ram_read(self.pc + 1),
            self.ram_read(self.pc + 2)
        ), end='')

        for i in range(8):
            print(" %02X" % self.reg[i], end='')

        print()

    # def run(self):
    #     """Run the CPU."""
    #     pass
