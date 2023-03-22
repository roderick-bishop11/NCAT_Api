package com.HBCU.controller

import com.HBCU.constants.ApplicationConstants
import com.HBCU.service.BasicService
import io.micronaut.http.annotation.Body
import io.micronaut.http.annotation.Controller
import io.micronaut.http.annotation.Post
import jakarta.inject.Inject

@Controller
class TestController(
    @Inject val basicService: BasicService
) {
    @Post(ApplicationConstants.ENDPOINT)
    fun double(@Body body: Body): String {
        return basicService.doubleIt(body.value)
    }

}