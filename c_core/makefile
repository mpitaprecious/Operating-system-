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