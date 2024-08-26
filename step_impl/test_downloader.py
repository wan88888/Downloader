import os
from time import sleep
from getgauge.python import before_spec, after_spec, after_step, step
import uiautomator2 as u2
from uuid import uuid1
from getgauge.python import custom_screenshot_writer


@before_spec
def before_feauture():
    global driver
    driver = u2.connect()
    driver.app_start("free.video.downloader.converter.music")
    driver.implicitly_wait(30)
    driver.watcher.when(
        '//*[@resource-id="free.video.downloader.converter.music:id/close_dialog_view"]').click()
    driver.watcher.start()


@after_spec
def after_feature():
    driver.watcher.stop()
    driver.app_stop("free.video.downloader.converter.music")


@step("当用户在首页搜索框输入<word>")
def step_impl(word):
    driver(resourceId="free.video.downloader.converter.music:id/tvSearch").click()
    driver.send_keys(word, clear=True)
    driver.press('enter')
    sleep(10)


@step("那么用户应该看到悬浮按钮亮起")
def step_impl():
    assert driver(
        resourceId="free.video.downloader.converter.music:id/tvGuide").exists()


@step("当用户在当前页面点击悬浮下载按钮")
def step_impl():
    driver(resourceId="free.video.downloader.converter.music:id/completeLoadView").click()
    sleep(2)


@step("那么用户应该看到下载进度页")
def step_impl():
    driver(resourceId="free.video.downloader.converter.music:id/tvTitle").exists()


@step("当用户在下载进度页点击关闭按钮")
def step_impl():
    driver(resourceId="free.video.downloader.converter.music:id/ivClose").click()


@step("而且用户点击底部工具栏主页按钮")
def step_impl():
    driver(resourceId="free.video.downloader.converter.music:id/ivGoHome").click()


@step("那么用户应该看到主页")
def step_impl():
    driver(resourceId="free.video.downloader.converter.music:id/tvGuide").exists()


@step("而且用户在当前页面点击坐标(<x>,<y>)")
def step_impl(x, y):
    driver.click(float(x), float(y))
    sleep(5)


@step("那么用户用户应该看到下载列表")
def step_impl():
    driver(resourceId="free.video.downloader.converter.music:id/downloadView").exists()


@step("当用户在下载列表点击Download按钮")
def step_impl():
    driver(resourceId="free.video.downloader.converter.music:id/downloadView").click()
    sleep(3)


@custom_screenshot_writer
def take_screenshot():
    file_name = os.path.join(
        os.getenv("gauge_screenshots_dir"), "screenshot-{0}.png".format(uuid1().int))
    image = driver.screenshot(file_name)
    return os.path.basename(image)