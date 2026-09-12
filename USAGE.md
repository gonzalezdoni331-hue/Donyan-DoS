# Advanced Usage

## How it works
MEDUSA uses a multi-threaded approach where each thread acts as an independent client. 

### Rate vs Threads
- **Threads**: The number of parallel connections.
- **Rate**: The frequency of requests per thread. 

To calculate total load:
`Total RPS = Threads * Rate`

## Proxy Support (Future)
Currently, the tool supports a basic proxy configuration via `proxy.txt`. 
In future versions, support for SOCKS5 and dynamic proxy rotation will be added.

## Error Handling
MEDUSA uses `try-except` blocks within the thread loop to ensure that a single timeout 
or connection error in one thread does not crash the entire attack process.