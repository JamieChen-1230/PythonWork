# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals

"""默認的"""
# class ChoutiLikeUpSpiderMiddleware(object):
#     # Not all methods need to be defined. If a method is not defined,
#     # scrapy acts as if the spider middleware does not modify the
#     # passed objects.
#
#     @classmethod
#     def from_crawler(cls, crawler):
#         # This method is used by Scrapy to create your spiders.
#         s = cls()
#         crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
#         return s
#
#     def process_spider_input(self, response, spider):
#         # Called for each response that goes through the spider
#         # middleware and into the spider.
#
#         # Should return None or raise an exception.
#         return None
#
#     def process_spider_output(self, response, result, spider):
#         # Called with the results returned from the Spider, after
#         # it has processed the response.
#
#         # Must return an iterable of Request, dict or Item objects.
#         for i in result:
#             yield i
#
#     def process_spider_exception(self, response, exception, spider):
#         # Called when a spider or process_spider_input() method
#         # (from other spider middleware) raises an exception.
#
#         # Should return either None or an iterable of Response, dict
#         # or Item objects.
#         pass
#
#     def process_start_requests(self, start_requests, spider):
#         # Called with the start requests of the spider, and works
#         # similarly to the process_spider_output() method, except
#         # that it doesn’t have a response associated.
#
#         # Must return only requests (not items).
#         for r in start_requests:
#             yield r
#
#     def spider_opened(self, spider):
#         spider.logger.info('Spider opened: %s' % spider.name)
#
#
# class ChoutiLikeUpDownloaderMiddleware(object):
#     # Not all methods need to be defined. If a method is not defined,
#     # scrapy acts as if the downloader middleware does not modify the
#     # passed objects.
#
#     @classmethod
#     def from_crawler(cls, crawler):
#         # This method is used by Scrapy to create your spiders.
#         s = cls()
#         crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
#         return s
#
#     def process_request(self, request, spider):
#         # Called for each request that goes through the downloader
#         # middleware.
#
#         # Must either:
#         # - return None: continue processing this request
#         # - or return a Response object
#         # - or return a Request object
#         # - or raise IgnoreRequest: process_exception() methods of
#         #   installed downloader middleware will be called
#         return None
#
#     def process_response(self, request, response, spider):
#         # Called with the response returned from the downloader.
#
#         # Must either;
#         # - return a Response object
#         # - return a Request object
#         # - or raise IgnoreRequest
#         return response
#
#     def process_exception(self, request, exception, spider):
#         # Called when a download handler or a process_request()
#         # (from other downloader middleware) raises an exception.
#
#         # Must either:
#         # - return None: continue processing this exception
#         # - return a Response object: stops process_exception() chain
#         # - return a Request object: stops process_exception() chain
#         pass
#
#     def spider_opened(self, spider):
#         spider.logger.info('Spider opened: %s' % spider.name)


"""測試下載中間件"""
class DownMiddleware1(object):
    def process_request(self, request, spider):
        """
            请求需要被下载时，经过所有下载器中间件的process_request调用
            :param request:
            :param spider:
            :return:
                None,继续后续中间件去下载；(後面的做，默認為None)
                Response对象，停止process_request的执行，开始执行process_response(我做完就好)
                Request对象，停止中间件的执行，将Request重新调度器
                raise IgnoreRequest异常，停止process_request的执行，开始执行process_exception(忽略此請求)
            """
        print("process_request1", request.url)
        pass

    def process_response(self, request, response, spider):
        """
        spider处理完成，返回时调用
        :param response:
        :param result:
        :param spider:
        :return:
            Response 对象：转交给其他中间件process_response
            Request 对象：停止中间件，request会被重新调度下载
            raise IgnoreRequest 异常：调用Request.errback
        """
        print('process_response1')
        return response


class DownMiddleware2(object):
    def process_request(self, request, spider):
        """
            请求需要被下载时，经过所有下载器中间件的process_request调用
            :param request:
            :param spider:
            :return:
                None,继续后续中间件去下载；(後面的做，默認為None)
                Response对象，停止process_request的执行，开始执行process_response(我做完就好)
                Request对象，停止中间件的执行，将Request重新调度器
                raise IgnoreRequest异常，停止process_request的执行，开始执行process_exception(忽略此請求)
            """
        print("process_request2", request.url)
        pass

    def process_response(self, request, response, spider):
        """
        spider处理完成，返回时调用
        :param response:
        :param result:
        :param spider:
        :return:
            Response 对象：转交给其他中间件process_response
            Request 对象：停止中间件，request会被重新调度下载
            raise IgnoreRequest 异常：调用Request.errback
        """
        print('process_response2')
        return response


"""測試爬蟲中間件"""
class SpiderMiddleware(object):

    def process_spider_input(self, response, spider):
        """
        下载完成，执行，然后交给parse处理
        :param response:
        :param spider:
        :return:
        """
        print("process_spider_input")

    def process_spider_output(self, response, result, spider):
        """
        spider处理完成，返回时调用
        :param response:
        :param result:
        :param spider:
        :return: 必须返回包含 Request 或 Item 对象的可迭代对象(iterable)
        """
        print("process_spider_output")
        return result

    def process_spider_exception(self, response, exception, spider):
        """
        异常调用
        :param response:
        :param exception:
        :param spider:
        :return: None,继续交给后续中间件处理异常；含 Response 或 Item 的可迭代对象(iterable)，交给调度器或pipeline
        """
        return None

    def process_start_requests(self, start_requests, spider):
        """
        爬虫启动时调用
        :param start_requests:
        :param spider:
        :return: 包含 Request 对象的可迭代对象
        """
        return start_requests
