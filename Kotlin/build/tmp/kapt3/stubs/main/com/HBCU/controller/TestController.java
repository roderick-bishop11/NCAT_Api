package com.HBCU.controller;

import java.lang.System;

@kotlin.Metadata(mv = {1, 6, 0}, k = 1, d1 = {"\u0000\u001e\n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0004\n\u0002\u0010\u000e\n\u0000\n\u0002\u0018\u0002\n\u0000\b\u0007\u0018\u00002\u00020\u0001B\r\u0012\u0006\u0010\u0002\u001a\u00020\u0003\u00a2\u0006\u0002\u0010\u0004J\u0012\u0010\u0007\u001a\u00020\b2\b\b\u0001\u0010\t\u001a\u00020\nH\u0007R\u0016\u0010\u0002\u001a\u00020\u00038\u0006X\u0087\u0004\u00a2\u0006\b\n\u0000\u001a\u0004\b\u0005\u0010\u0006\u00a8\u0006\u000b"}, d2 = {"Lcom/HBCU/controller/TestController;", "", "basicService", "Lcom/HBCU/service/BasicService;", "(Lcom/HBCU/service/BasicService;)V", "getBasicService", "()Lcom/HBCU/service/BasicService;", "double", "", "body", "Lio/micronaut/http/annotation/Body;", "demo"})
@io.micronaut.http.annotation.Controller
public final class TestController {
    @org.jetbrains.annotations.NotNull
    @jakarta.inject.Inject
    private final com.HBCU.service.BasicService basicService = null;
    
    public TestController(@org.jetbrains.annotations.NotNull
    com.HBCU.service.BasicService basicService) {
        super();
    }
    
    @org.jetbrains.annotations.NotNull
    public final com.HBCU.service.BasicService getBasicService() {
        return null;
    }
}