import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { AppComponent } from './app.component';
import { HttpClientModule } from '@angular/common/http';  // Importa o módulo HTTP

@NgModule({
  declarations: [
    AppComponent
  ],
  imports: [
    BrowserModule,
    HttpClientModule  // Adiciona o módulo HTTP
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
