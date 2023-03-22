package com.HBCU.service

import jakarta.inject.Singleton

@Singleton
class BasicService {

    fun doubleIt(value: String): String{
        val num = value.toInt()

        return (num*2).toString()
    }
}