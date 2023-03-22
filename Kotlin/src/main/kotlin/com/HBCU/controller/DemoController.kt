package com.HBCU.controller

import com.HBCU.constants.ApplicationConstants
import com.HBCU.service.BasicService
import io.micronaut.http.annotation.*
import jakarta.inject.Inject

@Controller
class DemoController(
    @Inject val basicService: BasicService
) {
    @Post(ApplicationConstants.ENDPOINT)
    fun double(@Body body: Body): String {
        return basicService.doubleIt(body.value)
    }


    @Get(ApplicationConstants.ENDPOINT)
    fun index(): String {

        return "Hello World!"
    }



}