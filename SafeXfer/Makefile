CC = gcc
CFLAGS = -Icommon -Wall -Wextra -O2

LDFLAGS_SERVER = -lssl -lcrypto -lpthread

SERVER_OBJS = server/main.o server/srvcore.o server/autoguard.o server/netdiscovery.o common/tlv.o
CLIENT_OBJS = client/main.o client/cli.o client/netdiscovery.o common/tlv.o

all: server client

server: $(SERVER_OBJS)
	$(CC) -o server/server $(SERVER_OBJS) $(LDFLAGS_SERVER)

client: $(CLIENT_OBJS)
	$(CC) -o client/client $(CLIENT_OBJS)

%.o: %.c
	$(CC) $(CFLAGS) -c $< -o $@

clean:
	rm -f server/server client/client $(SERVER_OBJS) $(CLIENT_OBJS)