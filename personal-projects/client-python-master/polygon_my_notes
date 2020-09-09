import time


from polygon import WebSocketClient, STOCKS_CLUSTER


def my_customer_process_message(message):
    print("this is my custom message processing", message)


def main():
    key = 'Wsd_l6Mcnd6capWLdFb_n_niG0SqxAmmHZ3VmJ'
    my_client = WebSocketClient(STOCKS_CLUSTER, key, my_customer_process_message)
    my_client.run_async()

    my_client.subscribe("T.MSFT", "T.AAPL", "T.AMD", "T.NVDA")
    time.sleep(2)

    my_client.close_connection()


if __name__ == "__main__":
    main()