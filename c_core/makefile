CC = gcc

CFLAGS = -Iinclude

LIBS = -lpthread

TARGET = eduos

SOURCES = main_sim.c process_manager.c thread_manager.c ipc_module.c

all:
	    $(CC) $(SOURCES) $(CFLAGS) -o $(TARGET) $(LIBS)

run:
	    .\$(TARGET).exe

clean:
	    del $(TARGET).exe


race:
	gcc race_demo.c -o race_demo -lpthread

fixed:
	gcc fixed_demo.c -o fixed_demo -lpthread